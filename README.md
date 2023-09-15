# Native Apps Templates
This repository contains templates released by Snowflake Inc for [Native App Framework](https://docs.snowflake.com/en/developer-guide/native-apps/native-apps-about).

## Available Templates
There are three available templates in the current version of this repository:
1. [basic](./basic/README.md)
2. [streamlit-python](./streamlit-python/README.md)
3. [streamlit-java](./streamlit-java/README.md)

For a detailed understanding of the templates, please refer to the README.md that comes with each of the templates. 

### Note
These templates are not an exhaustive list of use cases or possibilities that developers may want to explore when building Native Apps. 


## How to Use the Templates

There are two ways you can use the templates provided in this repository. 

1. Using SnowCLI (recommended)
    
    Run the following command in your terminal.
    ```
    snow app init <project_name> [--template={basic|streamlit-python|streamlit-java}]
    ```
    The command above is equivalent to the one below since `--template-repo` is optional if you intend to use any templates provided in this repository.  
    ```
    snow app init <project_name> [--template-repo=https://github.com/snowflakedb/native-apps-templates.git] [--template={basic|streamlit-python|streamlit-java}]
    ```

    For more information on using `snow app`, or SnowCLI in general, refer to [SnowCli](https://github.com/Snowflake-Labs/snowcli/). 

2. Using git clone

    You can also clone this repository manually and keep the template you would like to use. But as a note, any jinja files in this repository will not be rendered to their intended file type if using a simple git clone/no snowCLI. 
