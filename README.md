# Basic Python Web API

## Usage

**Starting Application**

- Download the code from GitHub.

`git clone git@github.com:sakipgur/python_api.git`

- Change directory to the new directory

`cd python_api`

- Build `docker-compose` environment

`docker-compose build`

- Run the environmet in detached mode

`docker-compose up -d`

**Testing Application**

- Open URL http://127.0.0.1:8080/ from browser and see `Hello!` message.

- Send a `GET` request to URL http://127.0.0.1:8080/healthz and see the return code and result.
From shell you should see something like below in json format:
```json
{
    "status": "OK",
    "version": "0.0.1",
    "uptime": "up since 2020-08-10 06:30:33 UTC"
}
```
