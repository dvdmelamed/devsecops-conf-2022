# Companion repository for the DevSecOps Conf 2022 talk about "Open Policy Agent (OPA) as a Control Engine"

## Content of the repository

This repository includes a simple Serverless application written in Python used to showcase 4 critical security controls integrated in the CI/CD pipeline (Github Actions) and Open Policy Agent as the decision layer 
whether or not the pipeline should fail. OPA pulls policy rules from another Github repository so that they are kept in an unique place for the whole organization (see the Github workflow for the url).

## Local setup

In order to use this project locally, you also need to setup localstack (provided as as a container in the `docker-compose` file).
Run the following command to start localstack:
```
docker-compose up -d
```

In addition, install the serverless framework globally using: `npm install -g serverless`, install the plugins using `npm install` and deploy the application to localstack using `sls deploy --stage local`.
You should see in the output the endpoint URL in the line under `endpoint`, e.g.
```
Serverless: Using serverless-localstack
Service Information
service: http-endpoint
stage: local
region: us-east-1
stack: http-endpoint-local
resources: 11
api keys:
  None
endpoints:
  http://localhost:4566/restapis/8m3g5k99q8/local/_user_request_
functions:
  currentTime: http-endpoint-local-currentTime
layers:
  None
```

To test the endpoint, use: 
```
curl http://localhost:4566/restapis/8m3g5k99q8/local/_user_request_/ping
```

or with a different timezone:
```
curl  "http://localhost:4566/restapis/8m3g5k99q8/local/_user_request_/ping?tz=Europe%2FLondon"
```

To run the Github workflow locally, install `act` using `npm install -g act` and run the workflow using:
```
act --artifact-server-path /tmp/ga-artifacts --artifact-server-port 34567 --bind
```

You should see at the end the following output:

```
[Security (push)/policy-evaluation]   💬  ::debug::Conftest exited with code 1.
[Security (push)/policy-evaluation]   💬  ::debug::stdout: FAIL - /Users/davidmelamed/dev/playground/secure-app/bandit-report.json - sast - SAST Test failed: 1 medium severitie(s)%0A%0A2 tests, 1 passed, 0 warnings, 1 failure, 0 exceptions%0A
[Security (push)/policy-evaluation]   💬  ::debug::stderr:
[Security (push)/policy-evaluation]   💬  ::debug::exitcode: 1
[Security (push)/policy-evaluation]   ⚙  ::set-output:: stdout=FAIL - /Users/davidmelamed/dev/playground/secure-app/bandit-report.json - sast - SAST Test failed: 1 medium severitie(s)

2 tests, 1 passed, 0 warnings, 1 failure, 0 exceptions
[Security (push)/policy-evaluation]   ⚙  ::set-output:: stderr=
[Security (push)/policy-evaluation]   ⚙  ::set-output:: exitcode=1
[Security (push)/policy-evaluation]   ✅  Success - conftest test ${{ github.workspace}}/bandit-report.json -n sast
[Security (push)/policy-evaluation] ⭐  Run exit ${{ steps.test-sast-policy.outputs.exitcode }}
[Security (push)/policy-evaluation]   🐳  docker exec cmd=[bash --noprofile --norc -e -o pipefail /Users/davidmelamed/dev/playground/secure-app/workflow/check-sast-policy-exit-code] user= workdir=
[Security (push)/policy-evaluation]   ❌  Failure - exit ${{ steps.test-sast-policy.outputs.exitcode }}
Error: exit with `FAILURE`: 1
```
