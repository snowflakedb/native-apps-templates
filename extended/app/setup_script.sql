-- This is the setup script that will run while installing your application instance in a consumer's account.
-- For more information on how to create setup file, visit https://docs.snowflake.com/en/developer-guide/native-apps/creating-setup-script

CREATE APPLICATION ROLE app_public;
CREATE OR ALTER VERSIONED SCHEMA core;
GRANT USAGE ON SCHEMA core TO APPLICATION ROLE app_public;

CREATE or REPLACE FUNCTION core.add(num1 NUMBER, num2 NUMBER)
  RETURNS NUMBER
  LANGUAGE JAVA
  IMPORTS = ('/module-add/add-1.0-SNAPSHOT.jar')
  HANDLER='Add.two';

GRANT USAGE ON FUNCTION core.add(NUMBER, NUMBER) TO APPLICATION ROLE app_public;

CREATE STREAMLIT core.add
     FROM '/streamlit/'
     MAIN_FILE = 'ui.py';

GRANT USAGE ON STREAMLIT core.add TO APPLICATION ROLE app_public;
