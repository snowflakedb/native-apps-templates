# This is where you can create python functions, which can further
# be used to create Snowpark UDFs and Stored Procedures in your setup_script.sql file.

from snowflake.snowpark import Session
from snowflake.snowpark.functions import lit

# UDF example:
def add_fn(x: int, y: int) -> int:
    return x + y


# Stored Procedure example:
def increment_by_one_fn(session: Session, x: int) -> int:
    df = session.create_dataframe([[]]).select((lit(1) + lit(x)).as_('RESULT'))
    return df.collect()[0]['RESULT']
