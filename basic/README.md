## Introduction

This is the basic project template for a Snowflake Native Apps project. It contains minimal code meant to help you set up your first application instance in your account quickly.

### Project Structure
| File Name | Purpose |
| --------- | ------- |
| README.md | The current file you are looking at, meant to guide you through a native apps project. |
| app/setup_script.sql | Contains SQL statements that are run when an account installs or upgrades an application. |
| app/manifest.yml | Defines properties required by the application package. Find more details at the [Manifest Documentation.](https://docs.snowflake.com/en/developer-guide/native-apps/creating-manifest)
| app/README.md | Exposed to the account installing the application with details on purpose and how to use the application. |
| snowflake.yml | Used by the snowCLI tool to discover your project's code and interact with snowflake with all relevant permissions and grants. |

### Adding a snowflake.local.yml file
Though your project directory already comes with a `snowflake.yml` file, an individual developer can choose to customize the behavior of the snowCLI by providing local overrides to `snowflake.yml`, such as a new role to test out your own application package. This is where you can use `snowflake.local.yml`, which is not a version-controlled file.

For more information, please refer to the Snowflake Documentation on installing and using SnowCLI to create Native Applications. 