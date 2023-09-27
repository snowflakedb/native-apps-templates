# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Hello Snowflake!")
st.write(
   """The sum of the two numbers are calculated by the Java Add.two() function
      which is called from code_schema.add() UDF defined in your setup_script.sql.
   """
)

num1 = st.number_input('First number', value=1)
num2 = st.number_input('Second number', value=1)

# Get the current credentials
session = get_active_session()

#  Create an example data frame
data_frame = session.sql("SELECT code_schema.add(%s, %s);" % (num1, num2))

# Execute the query and convert it into a Pandas data frame
queried_data = data_frame.to_pandas()

# Display the Pandas data frame as a Streamlit data frame.
st.dataframe(queried_data, use_container_width=True)