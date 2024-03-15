# ETL encapsulation in aws-Lambda Function with Serverless, CloudFormation, APIGateway, Docker, FastAPI to  PowerBI API 

This repository outlines the implementation of a real-time data streaming process from a public API to a Power BI dashboard using AWS Lambda, API Gateway, and FastAPI.

![Project_architecture.png](Assets%2FProject_architecture.png)

## Table of Contents

- [Project Overview](#project-overview)
- [Technical Architecture](#technical-architecture)
- [Prerequisites](#prerequisites)
- [Setup and Deployment](#setup-and-deployment)
- [Usage](#usage)
- [Improvements and Issues](#improvements-and-issues)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

In this exploration, I took a deep dive into real-time data streaming to a Power BI dashboard, utilizing AWS Lambda and API Gateway as my playground. The initiative? To venture beyond the familiar; because stretching beyond our comfort zones often leads to the most enlightening discoveries.

The project's heart lay in the streaming API of Power BI—a challenge to harness real-time data within AWS's rich landscape. Lambda, with its adaptability, stood at the forefront of this venture, a staple in the DevOps toolkit that I aimed to leverage. To add another layer of complexity and learning, I decided to step away from the trusted Spring Boot and embrace FastAPI for its promise of scalable and straightforward execution.

Choosing a public API as the data fountain, I envisioned a Power BI dashboard dynamically coming to life with varied data streams—a dashboard that evoked thoughts on how similar tools might be used by organizations to monitor diverse datasets.

## Technical Architecture

Structured in a modular approach, this project includes FastAPI setup, Lambda function handling, and the serverless framework for deployment. The repository reflects the folder structure for clear separation of concerns.

## Prerequisites

- AWS CLI configured with the appropriate access
- FastAPI for local API testing
- Serverless Framework for deployment
- Docker Desktop installed to dockerize all the dependencies
- PyCharm or similar IDE for development
- An S3 bucket for storing dependencies

## Setup and Deployment

1. **FastAPI Setup:** Enable local API testing and endpoint interaction.
2. **Serverless Configuration:** Utilize `serverless.yml` to configure and deploy the AWS Lambda function and API Gateway.
3. **S3 Bucket Creation:** Required for storing the zipped dependencies.
4. **Local Testing:** Using AWS CLI for deployment and PyCharm for code development.
5. **Lambda Layer:** Confirm the creation and association of the layer through the AWS Management Console or AWS CLI.

## Usage

Invoke the deployed Lambda function through the API Gateway endpoint to initiate the ETL process and monitor the data streaming to Power BI.
For more details take a look to my article:
[Medium](URL)
[Linkedin](URL)


## Improvements and Issues

While the function currently faces a 30-second timeout due to API Gateway constraints, potential improvements include using AWS SQS and DynamoDB for extended processing times.

## Contributing

Contributions to enhance the functionality, improve documentation, or fix issues are welcome. Please open an issue or submit a pull request.
Or support my contributions with buying me a coffe: https://www.buymeacoffee.com/rafael.vera

## Acknowledgments

I'd like to express my sincere gratitude to all contributors and mentors who have supported this project and of course the to the community and to my family for their patience and support.

