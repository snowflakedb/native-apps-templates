## Introduction

This is an example template for a Snowflake Native Apps project which demonstrates the use of Java extension code and adding Streamlit code. This template is meant to guide developers towards a possible project structure on the basis on functionality, as well as indicate the contents of some common and useful files. 

# How to build/test this template
## Build the jar
You need to build the Java application (module-add) to get the .jar file, assuming JDK and Maven are installed and properly configured. 
```
cd src/module-add/
mvn clean install
mvn package
```

Similarly, you can also use your own build steps for any other languages supported by Snowflake that you wish to write your code in, and any build automation tools you prefer. For more information on supported languages, visit [docs](https://docs.snowflake.com/en/developer-guide/stored-procedures-vs-udfs#label-sp-udf-languages).

## Run the app
Create or update an Application Package in your Snowflake account, upload application artifacts to a stage in the application package, and create or update an Application instance based on the uploaded artifacts.
```
snow app run
```

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
   |          |    |-java/com/snowflake/add
   |          |                           |-Add.java
   |          |
   |          |-test
   |               |-java/com/snowflake/add
   |                                      |-AddTest.java
   |module-ui
   |        |-src
   |            |-ui.py
   |            |-environment.yml
```

## `snowflake.yml.jinja`
While this file exists as a Jinja template, it is the only file that will be automatically rendered as a `snowflake.yml` file by the `snow app init` command, as described in the [README.md](../README.md). `snowflake.yml` is used by the snowCLI tool to discover your project's code and interact with snowflake with all relevant permissions and grants. Below are some of the configuration keys that you can use in `snowflake.yml` file.

### `native_app.name`
**Required: Yes**<br/>
**Example value: `myapp`**<br/>
**Default: `<native_app_project_directory_name>`**<br/>
An identifier you can refer to this project by. Allows SnowCLI to detect if an associated application package (derived from this name) exists in connected accounts and prevents tooling from interacting with unrelated (but identically named) objects in an account, by tagging the application / application package as belonging to this project. The file called `snowflake.yml.jinja` will be rendered as `snowflake.yml` file with the name of your Native App project as the default value to this field. 

### `native_app.deploy_root`
**Required: No**<br/>
**Default: `output/deploy/`**<br/>
This will be a folder where all artifacts from your build step will be copied to. These artifacts are ready to be deployed to a Snowflake stage, described below. 

### `native_app.source_stage`
**Required: No**<br/>
**Default: `app_src.stage`**<br/>
This is the identifier to a stage that will hold the application artifacts. It is specified as `<schema_name>.<stage_name>` and lives within the Application Package object. It is customizable so that name collisions can be prevented.

### `native_app.package.scripts`
**Required: No**<br/>
**Example values:** <br/>
\- package/schema1.sql<br/>
\- package/schema2.sql

List of SQL file paths relative to the project root. These files are executed as the provider whenever you deploy your application package, e.g. to populate shared content. As such, they must be idempotent.


### `native_app.artifacts`
**Required: Yes**<br/>
**Example values:**<br/>
```
- src: app/*
  dest: ./
- src: streamlit/*
  dest: streamlit/
- src: src/resources/images/snowflake.png
  dest: streamlit/
```

List of source / destination pairs for files to be added to the deploy root.

If src refers to just one file (not a glob), dest can refer to a target path or a path + name (to support renaming).

Destination paths must end with “/”; if a glob pattern’s destination does not end with a “/”, this will be treated as an error. If omitted, “dest” defaults to the same string as “src”.

Short-form: can also pass in a string for each list item instead of a dict; in this case, the value is treated as both “src” and “dest”.


### `native_app.package.role`
**Required: No**<br/>
**Default: _Resolved connection role_**<br/>
The role used to create the application package / provider-side objects. If empty, the role specified on the SnowCLI connection will be used.
_Note: typically specified in snowflake.local.yml, described in the last section._

### `native_app.package.name`
**Required: No**<br/>
**Default: _{native_app.name}\_pkg\_$USER_**<br/>
The name used to create / reference the application package that will be created when you run “snow app run”.
`$USER` can be ordinary `$USER`, `$USERNAME` or `$LOGNAME` environment variables, depending on your platform. 
_Note: typically specified in snowflake.local.yml, described in the last section._

### `native_app.application.role`
**Required: No**<br/>
**Default: _Resolved connection role_**<br/>
The role used to create the application instance / consumer-side objects. If empty, the role specified on the SnowCLI connection will be used.
_Note: typically specified in snowflake.local.yml, described in the last section._

### `native_app.application.name`
**Required: No**<br/>
**Default: _{native_app.name}\_$USER_**<br/>
The name used to create / reference the (loose files) application that will be created when you run “snow app run“.
`$USER` can be ordinary `$USER`, `$USERNAME` or `$LOGNAME` environment variables, depending on your platform. 
_Note: typically specified in snowflake.local.yml, described in the last section._

### `native_app.application.warehouse`
**Required: No**<br/>
**Default: _Resolved connection warehouse_**<br/>
The warehouse used to install the application. If empty, the warehouse specified on the SnowCLI connection will be used. If no warehouse is specified there, it is not a validation error, but the application will fail to install.
_Note: typically specified in snowflake.local.yml, described in the last section._

### `native_app.application.debug`
**Required: No**<br/>
**Default: True**<br/>
Whether the debug mode is enabled, when the application is installed using the loose files mode.

## Adding a snowflake.local.yml file
Though your project directory must have a `snowflake.yml` file, an individual developer can choose to customize the behavior of the snowCLI by providing local overrides to `snowflake.yml`, such as a new role to test out your own application package. This is where you can use `snowflake.local.yml`, which is not a version-controlled file.

Create a `snowflake.local.yml` file with relevant values to the fields, defaults are described in the preceding section.
```
native_app:
  package:
    role: <your_app_pkg_owner_role>
    name: <name_of_app_pkg>

  application:
    role: <your_app_owner_role>
    name: <name_of_app>
    debug: <true|false>
    warehouse: <your_app_warehouse>

```