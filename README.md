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
Dockerfile.nginx: Builds the Nginx image with two server blocks.
Dockerfile.test: Builds a test image that verifies the responses from each server block.
docker-compose.yml: Manages both containers using Docker Compose.
GitHub Actions Workflow: Automates the build, test, and artifact creation process.



