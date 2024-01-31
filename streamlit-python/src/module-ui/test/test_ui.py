import pytest
from snowflake.snowpark import Session
from snowflake.snowpark.column import ColumnOrLiteral, Column
from snowflake.snowpark.functions import lit
from streamlit.testing.v1 import AppTest
from unittest.mock import patch
from add import increment_by_one_fn
import ui as ui

@pytest.fixture()
def session():
    session = Session.builder.config('local_testing', True).create()
    yield session
    session.close()

test_core_add_result = 9

def mock_call_udf(udf_name: str, *args: ColumnOrLiteral):
    if udf_name == 'core.add':
        return lit(test_core_add_result)
    else:
        raise NotImplementedError
    
def mock_call_sproc(session: Session, sproc_name: str, *args):
    if sproc_name == 'core.increment_by_one':
        return increment_by_one_fn(session, args[0])
    else:
        raise NotImplementedError

@patch('snowflake.snowpark.session.Session.call', autospec=True)
@patch('snowflake.snowpark.functions.call_udf')
@patch('snowflake.snowpark.context.get_active_session')
def test_streamlit(get_active_session, call_udf, call_sproc, session: Session):
    get_active_session.return_value = session
    call_udf.side_effect = mock_call_udf
    call_sproc.side_effect = mock_call_sproc

    at = AppTest.from_function(ui.run_streamlit)
    at.run()

    at.number_input('numToAdd1').set_value(6).run()
    at.number_input('numToAdd2').set_value(3).run()
    assert (at.dataframe[0].value[:].values == [[test_core_add_result]]).all()

    at.number_input('numToIncrement').set_value(4).run()
    assert (at.dataframe[1].value[:].values == [[5]]).all()
    assert not at.exception
