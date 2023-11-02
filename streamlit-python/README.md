## Introduction

This is an example template for a Snowflake Native Apps project which demonstrates the use of Python extension code and adding Streamlit code. This template is meant to guide developers towards a possible project structure on the basis on functionality, as well as indicate the contents of some common and useful files. 

Since this template contains python files only, you do not need to build the source code with any additional step. You can directly go to the next section. However, if there were any source code that needed to be built, you would manually perform the build steps here before proceeding to the next section. 

Similarly, you can also use your own build steps for any other languages supported by Snowflake that you wish to write your code in. For more information on supported languages, visit [docs](https://docs.snowflake.com/en/developer-guide/stored-procedures-vs-udfs#label-sp-udf-languages).

## Run the app
Create or update an Application Package in your Snowflake account, upload application artifacts to a stage in the application package, and create or update an Application instance based on the uploaded artifacts.
```
snow app run
```

Please refer to the online Snowflake Documentation on using SnowCLI to create Native Applications for more information on this. 

# Directory Structure
## `/app`
This directory holds your Snowflake Native App files.

### `/app/README.md`
Exposed to the account installing the application with details on purpose and how to use the application.

### `/app/manifest.yml`
Defines properties required by the application package. Find more details at the [Manifest Documentation.](https://docs.snowflake.com/en/developer-guide/native-apps/creating-manifest)

### `/app/setup_script.sql`
Contains SQL statements that are run when an account installs or upgrades an application.

## `/scripts`
You can add any additional scripts such as `.sql` and `.jinja` files here. One of the common use cases for such a script is to be able to add shared content from external databases to your application package, which makes it available to be used in the setup script that runs during application installation. 
_Note: As of now, `snow app init` does not render these jinja templates for you into the required files, if you decide to use them. You will have to manually render them for now._


## `/src`
This directory contains code organization by functionality, such as one distinct module for Streamlit related code, and another module for "number add" functionality, which is used an example in this template. 
```
/src
   |-module-add
   |          |-main
   |          |    |-python
   |          |           |-add.py
   |          |
   |          |-test
   |               |-python
   |                      |-add_test.py
   |
   |module-ui
   |        |-src
   |            |-ui.py
   |            |-environment.yml
```

## `snowflake.yml.jinja`
While this file exists as a Jinja template, it is the only file that will be automatically rendered as a `snowflake.yml` file by the `snow app init` command, as described in the [README.md](../README.md). `snowflake.yml` is used by the snowCLI tool to discover your project's code and interact with snowflake with all relevant permissions and grants. Below are some of the configuration keys that you can use in `snowflake.yml` file.

Please refer to the online Snowflake Documentation on using SnowCLI to create Native Applications for more information on this. 

## Adding a snowflake.local.yml file
Though your project directory must have a `snowflake.yml` file, an individual developer can choose to customize the behavior of the snowCLI by providing local overrides to `snowflake.yml`, such as a new role to test out your own application package. This is where you can use `snowflake.local.yml`, which is not a version-controlled file.

Please refer to the online Snowflake Documentation on using SnowCLI to create Native Applications for more information on this. 