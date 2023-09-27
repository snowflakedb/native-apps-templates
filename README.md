# Native Apps Templates
This repository contains templates released by Snowflake Inc for [Native App Framework](https://docs.snowflake.com/en/developer-guide/native-apps/native-apps-about).

## Available Templates
There are two available template in the current version of this repository:
1. [basic](./basic/README.md)
2. [extended](./extended/README.md)

For a detailed understanding of the templates, please refer to the README.md that comes with each of the templates. 

## How to Use the Templates

There are two ways you can use the templates provided in this repository. 

1. Using SnowCLI (recommended)
    
    Run the following command in your terminal.
    ```
    snow app init <project_name> [--template={basic|extended}]
    ```
    The command above is equivalent to the one below since `--template-repo` is optional if you intend to use any templates provided in this repository.  
    ```
    snow app init <project_name> [--template-repo=https://github.com/Snowflake-Labs/native-apps-templates.git] [--template={basic|extended}]
    ```

    For more information on using `snow app`, or SnowCLI in general, refer to [SnowCli](https://github.com/Snowflake-Labs/snowcli/). 

2. Using git clone

    You can also clone this repository manually and keep the template you would like to use. But as a note, any jinja files in this repository will not be rendered to their intended file type if using a simple git clone/no snowCLI. 
