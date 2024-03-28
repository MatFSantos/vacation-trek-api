# VACATION TREK API

This repository refers to the REST API of the Vacation Trek project, a website for organizing vacation plans.

With this site, the user can plan their vacation in the best possible way, registering the destinations and companies that will enjoy the moment.


## How to run locally

First you'll must configure the environments variables, running the following command line:

```
$ cp .env.example .env
```
> This command will be copy all content present in environment file example and create a new environment file.

After that, put the database URL in the generated `.env`. Example:
```
...
DB_URL="<database>://<user>:<password>@<address>:<port>/<database_name>"
...
```
> This is a generic URL. If you'll use docker to run the application, use the following database URL: `DB_URL="postgres://admin:admin@postgres:5432/postgres"`

In addition the database URL, you can change other parameters like the `APP_PORT`, the `EXPIRES_TOKEN` and the `ALGORITHM_TOKEN`. But this change is not mandatory, as these have default values.

The next step is generate de application key. For that, run the following command:

```
$ python key_gen.py
```

### To run with Docker

To run with Docker, you must have Docker installed in your machine. After that, run this command:

```
$ sudo docker compose up -d
```

> This command will be create the image to `postgres` and the entire application and run in the background. You can stop the process running `sudo docker stop vacation-trek-api postgres`.

Now yout API is runing in `http://localhost:3333`.

### To run without Docker

You must ensure that you have a postgresql on your machine or  in the cloud, and that you have correctly placed the database URL in the `.env` file.

After ensured this, run the following command:

```
$ pip install pipenv
```
```
$ pipenv install --dev
```
```
$ pipenv shell
```

> pipenv is a tool to create a virtual environment for the application. The three commands will install the pipenv tool, install all dependencies of the project and start the environment, respectively.

Once the environment started and all dependencies have been installed, the database migrations must be carried out by running the following commands:

```
$ prisma migrate dev
```

```
$ prisma generate
```

> These commands will migrate and generate the prisma models.

Now, to run the application just execute:

```
$ python run.py
```