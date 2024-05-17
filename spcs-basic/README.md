# Instructions

## Set your SnowCLI connection (optional)

We use your default connection to connect to Snowflake and deploy the images / app. Set your
default connection in your `config.toml` or by exporting the following environment variable:

```sh
export SNOWFLAKE_DEFAULT_CONNECTION_NAME=na_provider_consumer_qa6
```

## Create image repository, build and push our local service image

The [service/](service/) directory contains a [Dockerfile](service/Dockerfile) that builds a
simple Python server that responds to GET health checks, a GET for `/index.html`, as well as
POSTing to `/echo` in the Snowflake External Function payload format. You can build it and
push it to an image repository in your count like so:

```sh
./build-and-push.sh
```

This command will always use your default SnowCLI connection.

## Deploy the application

Deploy the app package and instance as such:

```sh
snow app run
```

## Setup the application

When the application is opened for the first time, you need to grant some `Account Privileges`

- CREATE COMPUTE POOL
- BIND SERVICE ENDPOINT

Click on the `Grant` button to proceed.

## Activate the application

Once privileges are granted, a new `Activate` button should appear. Click the button and wait until the application is fully activated.
The `Activate` button invokes the `grant_callback` defined in the [manifest.yml](app/manifest.yml) file and creates the `COMPUTE POOL`s and `SERVICE`s needed to launch the application.

## Launch the application

Once all services and pools are created, you are able to launch the app by clicking on the `Launch App` button. A new window will be displayed with the URL provided by the `Service` and `Endpoint` defined in the `default_web_endpoint` in the [manifest.yml](app/manifest.yml).

## Test out the echo service

```sh
snow sql -q "select spcs_na_$USER.services.echo('Hello world!')"
```

You should see the same text back (Hello world!).

## Clean up

Your service and compute pool is costing you money. Make sure to clean up.

```sh
snow sql -q "call spcs_na_$USER.setup.drop_service_and_pool()"
```

Optionally, you can remove the app + package altogether afterwards.

```sh
snow app teardown
```
