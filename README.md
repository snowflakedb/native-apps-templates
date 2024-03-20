# Snowflake Native App Templates with Snowflake CLI
**Note**: Snowflake CLI is in Public Preview (PuPr). You can find the official documentation [here](https://docs.snowflake.com/en/developer-guide/snowflake-cli-v2/index).

This repository contains [Snowflake Native App](https://docs.snowflake.com/en/developer-guide/native-apps/native-apps-about) templates released by Snowflake Inc. These templates are customized to work with Snowflake CLI. 

## Available Templates
There are three available templates in the current version of this repository:
1. [basic](./basic/README.md)
2. [streamlit-python](./streamlit-python/README.md)
3. [streamlit-java](./streamlit-java/README.md)

For a detailed understanding of the templates, please refer to the README.md within each template. 

### Note
These templates are not an exhaustive list of use cases or possibilities that developers may want to explore when building their Snowflake Native App. 


## How to Use the Templates

There are two ways you can use the templates provided in this repository. 

1. Using Snowflake CLI (recommended)

    For more information, please refer to the [Snowflake CLI Documentation](https://docs.snowflake.com/en/developer-guide/snowflake-cli-v2/index) on installing and using Snowflake CLI to create a Snowflake Native App. 
    
    Once Snowflake CLI is installed and configured, run the following command in your terminal.
    ```
    snow app init <project_name> [--template={basic|streamlit-python|streamlit-java}]
    ```
    The command above is equivalent to the one below since `--template-repo` is optional if you intend to use any templates provided in this repository.  
    ```
    snow app init <project_name> [--template-repo=https://github.com/snowflakedb/native-apps-templates.git] [--template={basic|streamlit-python|streamlit-java}]
    ```

2. Using git clone

    You can also clone this repository manually and keep the template you would like to use. But as a note, any jinja files in this repository will not be rendered to their intended file type if using this option. 
