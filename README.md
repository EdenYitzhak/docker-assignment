# Docker Assignment

## Overview
This project demonstrates a setup of two Docker containers orchestrated using `docker-compose`. 
The first container runs an Nginx server with two server blocks:
1. **Server Block 1**: Responds on port 8080- returns a custom plain text message with a 200 OK status.
2. **Server Block 2**: Responds on port 8081- returns a custom plain text error message with a 404 Not Found status.

The second container is a testing container, written in Python, that checks the responses from both Nginx server blocks to ensure they behave as expected.

This setup is automatically built and tested in a GitHub Actions CI workflow. Upon a successful test, an artifact is published as "succeeded," otherwise, it is labeled as "fail."

## Project Structure
```plaintext
├── docker-compose.yml             # Defines the two services: nginx-server and nginx-tester
├── nginx/
│   ├── Dockerfile.nginx           # Dockerfile for the Nginx server image
│   └── nginx.conf                 # Nginx configuration with two server blocks
├── tester/
│   ├── Dockerfile.test            # Dockerfile for the testing container
│   └── test_nginx.py              # Python script to test the Nginx server responses
└── .github/
    └── workflows/
        └── ci.yml                 # GitHub Actions CI workflow for building, testing, and publishing artifacts
```
## Project Structure
***Dockerfile.nginx:*** Builds the Nginx image with two server blocks.  
***Dockerfile.test:*** Builds a test image that verifies the responses from each server block.  
***docker-compose.yml:*** Manages both containers using Docker Compose.  
***GitHub Actions Workflow:*** Automates the build, test, and artifact creation process.  

## CI Workflow
The CI workflow is defined in `.github/workflows/ci.yml` to:

1.Build both Docker images.  
2.Run tests on each Nginx server endpoint.  
3.Upload a result file indicating the success or failure of the tests.  

## Issue and Solution
**Problem**: The CI workflow would get "stuck" and not move to the next steps after running the tests. This happened because docker-compose up waits for all containers to stop before finishing. In our setup, the nginx-server container kept running even after the nginx-tester container (which performs the tests) finished.

**Solution**: To solve this, I added the --abort-on-container-exit option to docker-compose up. This makes Docker Compose exit as soon as the nginx-tester container completes. This way, the workflow moves to the next steps without hanging.

```
- name: Build and Test Containers
  run: |
    docker compose -f docker-compose.yml up --build --abort-on-container-exit
    if [ $? -eq 0 ]; then
      echo "succeeded" > result.txt
      echo "Test passed: Both Nginx servers responded as expected." >> result.txt
      echo "- Server 1 returned custom plain text response" >> result.txt
      echo "- Server 2 returned HTTP 404 Not Found response" >> result.txt
    else
      echo "fail" > result.txt
    fi
```
This command ensures that the workflow continues smoothly to the final steps once the tests are complete.

***Note:***
You can find the build itself in the Actions tab, and you can also download the ```.txt``` file there.
![image](https://github.com/user-attachments/assets/04f08d1b-1ccf-4cfd-ad9b-1fd31f00983b)


![image](https://github.com/user-attachments/assets/902e0a1b-9922-4ba0-b991-64a1f965b27e)


![image](https://github.com/user-attachments/assets/d166db34-bba7-4e04-aa80-39a4c71b61b5)


