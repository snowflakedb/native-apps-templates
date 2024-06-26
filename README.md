# Snowflake Native App Templates with Snowflake CLI
**Note**: Snowflake CLI is in Public Preview (PuPr). You can find the official documentation [here](https://docs.snowflake.com/en/developer-guide/snowflake-cli-v2/index).

This repository contains [Snowflake Native App](https://docs.snowflake.com/en/developer-guide/native-apps/native-apps-about) templates released by Snowflake Inc. and are designed to work with Snowflake CLI.

## Available Templates
The current list of templates is as follows:

1. [basic](./basic/README.md) (default)
2. [spcs-basic](./spcs-basic/README.md)
3. [streamlit-java](./streamlit-java/README.md)
4. [streamlit-javascript](./streamlit-javascript/README.md)
5. [streamlit-python](./streamlit-python/README.md)

See the `README.md` file in the root of each template directory for more information.

### Note
These templates are not an exhaustive list of use cases or possibilities for building Snowflake Native Apps;
take a look at the [native-apps-examples](https://github.com/snowflakedb/native-apps-examples) repository for more fully-featured examples.

## How to Use the Templates

Snowflake CLI contains built-in functionality to initialize project directories on your local filesystem using the templates in this (or any other) repository. For example, to initialize a new Snowflake Native App project called `my-app` using the `spcs-basic` template, run the following command:

```bash
snow app init my-app --template spcs-basic
```

Please refer to the [Snowflake CLI Documentation](https://docs.snowflake.com/en/developer-guide/snowflake-cli-v2/index) for more information on installing and using Snowflake CLI.

### Note
You can also clone this repository manually using `git` and simply modify the template you would like to use.
Note that any files in this repository containing Jinja template tags will not be rendered to their intended file type if using this option. 
