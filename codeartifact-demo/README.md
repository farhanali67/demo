# CodeArtifact Maven and npm demo

This folder is isolated from the Flask application. It validates public dependency resolution through the `tappayments` CodeArtifact domain in `us-east-1`.

| Test | Repository | Public dependency |
| --- | --- | --- |
| `npm-test` | `npm-internal` | `lodash` |
| `maven-test` | `maven-internal` | Apache Commons Lang |

The provided `settings.xml` and `.npmrc.example` are templates. They contain no token and must not be used to store one. The Jenkinsfile creates short-lived configuration files and supplies them to Docker as BuildKit secrets.

## Jenkins demo

Create a Jenkins Pipeline job using `Jenkinsfile.codeartifact-demo`. Run it on an AWS Jenkins agent with the `docker-awscli` label and the attached CodeArtifact read policy.

The agent role supplies AWS credentials. The pipeline requests a temporary CodeArtifact token and never passes it through a Docker build argument.

