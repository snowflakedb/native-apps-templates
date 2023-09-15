This is template for [Snowflake Native Apps](https://docs.snowflake.com/en/developer-guide/native-apps/native-apps-about).

# How to build/test this template
## Build the jar
You need to build the Java application (module-add) to get the .jar file.
```
cd module-add/
mvn clean install
mvn package
```

## Bundle
Bundle the app package
```
snow app bundle
```

## Run the app
Test the app.
```
snow app run
```

# Directory Structure
## `/app`
This directory hold your Snowflake Native App files.

### `/app/README.md`
The README file for the native app instance.

### `/app/manifest.yml`
The manifest of your Native App. Visit [docs][https://docs.snowflake.com/en/developer-guide/native-apps/creating-manifest] for more information.

### `/app/setup_script.sql`
This is the setup script that will run while installing your application instance in a consumer's account.

### `/scripts`
You can add any additional scripts such as `.sql` and `.jinja` files here.

### `/src`
This directory hold your source code of different modules, such as streamlit apps, java code, python or any Snoflake supported language. For more information on supported languages, visit [docs](https://docs.snowflake.com/en/developer-guide/stored-procedures-vs-udfs#label-sp-udf-languages).
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
   |
   |module-ui
   |        |-src
   |            |-ui.py
```

## `snowflake.yml`
`snowflake.yml` files holds the configuration to your Snowflake Native App. Below are some of the configuration keys that you can use in `snowflake.yml` file.
### `native_app.name`
**Required: Yes**<br/>
**Example value: `myapp`**<br/>
An identifier you can refer to this project by. Allows SnowCLI to detect if an associated application package (derived from this name) exists in connected accounts and prevents tooling from interacting with unrelated (but identically named) objects in an account, by tagging the application / application package as belonging to this project

### `native_app.deploy_root`
**Required: No**<br/>
**Default: `output/deploy/`**<br/>
Where do build artifacts live that are ready to be deployed to Snowflake?

### `native_app.source_stage`
**Required: No**<br/>
**Default: `app_src.stage`**<br/>
What is the schema.name of the stage (inside the application package) that will hold application code? Customizable so that name collisions can be prevented.

### `native_app.package.scripts`
**Required: Yes**<br/>
**Example values:** <br/>
\- package/schema1.sql<br/>
\- package/schema2.sql

List of SQL file paths relative to the project root. These files are executed as the provider whenever you deploy your application package, e.g. to populate shared content. As such, they must be idempotent.

This can also be glob patterns, in which case files are executed in lexicographic order (within the glob; you can control ordering with more granularity by listing files manually).

### `native_app.artifacts`
**Required: Yes**<br/>
**Example value:**<br/>
```
- src: setup.sql
  dest: .
- src: manifest.yml
- src: app/README.md
- src: app/environment.yml
  dest: streamlit/
- src: streamlit/*
  dest: streamlit/
- src: image.jpg
  dest: streamlit/
```

What files should your bundle step depend on / be added to the deploy root? List of source / destination pairs.

If src refers to just one file (not a glob), dest can refer to a target path or a path + name (to support renaming).

Destination paths must end with “/”; if a glob pattern’s destination does not end with a “/”, this will be treated as an error. If omitted, “dest” defaults to the same string as “src”.

Short-form: can also pass in a string for each list item instead of a dict; in this case, the value is treated as both “src” and “dest”.


### `native_app.package.role`
**Required: No**<br/>
**Default: _Resolved connection role_**<br/>
Which role should be used to create the application package / provider-side objects? If empty, the role specified on the SnowCLI connection will be used.
_Note: Connection-specific; should not usually be included in snowflake.yml directly._

### `native_app.package.name`
**Required: No**<br/>
**Default: _{escape(native_app.name)}_pkg_USER_**<br/>
What is the name that should be used to create / reference the application package that will be created when you run “snow app dev”?
_Note: Connection-specific; should not usually be included in snowflake.yml directly._

### `native_app.application.role`
**Required: No**<br/>
**Default: _Resolved connection role_**<br/>
Which role should be used to create the application instance / consumer-side objects? If empty, the role specified on the SnowCLI connection will be used.
_Note: Connection-specific; should not usually be included in snowflake.yml directly._

### `native_app.application.name`
**Required: No**<br/>
**Default: _{escape(native_app.name)}_USER_**<br/>
What name should be used to create / reference the (loose files) application that will be created when you run “snow app dev“?
_Note: Connection-specific; should not usually be included in snowflake.yml directly._

### `native_app.application.warehouse`
**Required: No**<br/>
**Default: _Resolved connection warehouse_**<br/>
What warehouse should be used to install the application? If empty, the warehouse specified on the SnowCLI connection will be used. If no warehouse is specified there, it is not a validation error, but the application will fail to install.
_Note: Connection-specific; should not usually be included in snowflake.yml directly._

### `native_app.application.debug`
**Required: No**<br/>
**Default: True**<br/>
Should installed applications be created with debug mode enabled? This applies only to loose files installation modes.
