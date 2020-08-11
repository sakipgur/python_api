# Basic Python Web API

## Usage

**Starting Application**

- Download the code from GitHub.

`$ git clone git@github.com:sakipgur/python_api.git`

- Change directory to the new directory

`$ cd python_api`

- Build `docker-compose` environment

`$ docker-compose build`

- Run the environmet in detached mode

`$ docker-compose up -d`

**Testing Application**

- Open URL http://localhost:8080/ from browser and see `Hello!` message.

- Send a `GET` request to URL http://localhost:8080/healthz and see the return code and result.
Return code should be `200` and output should be similar to below json output.

```json
{
    "status": "OK",
    "version": "0.0.1",
    "uptime": "up since 2020-08-10 06:30:33 UTC"
}
```
## Automation Process

**Branching**

I plan to use feature branching strategy. So we will be allowing developers to create a branch for each feature or task. For example adding new API or changing an existing one. When they are done, their PRs will be merged to the main branch. Before merging we need to build the code for integrity and conflicts.

**Tools/Services to Use**

- Git: As our code version control system.

- Jenkins: We can use `Jenkins` as an orchestrator. Also we will be configurig `Pipeline` for that Jenkins `Job` choosing `Pipeline script` as the `Destination`. We will include all stages in this `Jenkinsfile` script. 

- GitHub: As our code repository. Will also include `Jenkinsfile`. So we will configure Jenkins job with `Pipeline script from SCM` option.

- DockerHub: For keeping docker artifacts that we created while building. Indeed all our code will be in GitHub.

- GCP: We need some infrastructure to deploy. In this project I also used docker-compose, so I can deploy almost anywhere. But because we will do automating we should be able to connect as service.

**Pipeline Stages**

- Environment: Global variables for the project
    * Define a image_tag

- Test: Test the code
    * Because it is python we can also check `flake8 --statistics` for indentations, before unit tests
    * Unit tests
    * Some selenium jobs maybe configured/triggered and run

- Build and push image(s) to Artifactory (DockerHub) with some image_tag.
    * Use image_tag for tagging
    * Push images to articatory or registry

- Deploy to Staging environment
    * Connect to Environment (here we need to setup credentials for GCP)
    * Initiate Kubernetes environment in GCP/or just initiate a single server instance
    * Run environment tests if needed.

- Deploy to Production
    * Deploying Production mostly needs Change Management system to be placed.
