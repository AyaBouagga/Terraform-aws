

<p align="center">
  ![Image description](https://github.com/AyaBouagga/Terraform-aws/blob/test/images.png)
</p>

# Lambda OpenSearch Integration Project

This project provides a pipeline for processing logs or event data using AWS Lambda and OpenSearch (formerly Elasticsearch). The goal is to enable real-time data ingestion into OpenSearch for querying, analytics, and visualization.

## Project Overview

The project sets up an AWS infrastructure where:

1. **Logs or Event Data**: Application logs or event data are sent to a Lambda function.
2. **Data Processing**: The Lambda function processes incoming data and forwards it to an OpenSearch domain.
3. **OpenSearch**: Data is indexed into OpenSearch, enabling querying, filtering, and visualization through Kibana.

## Architecture

The project leverages the following AWS components:

- **AWS Lambda**: Handles the data processing and ingestion logic.
- **AWS OpenSearch**: Acts as the search and analytics engine where data is indexed and stored.
- **AWS IAM**: Manages secure access between the Lambda function and OpenSearch.
- **Terraform**: Used for defining and provisioning the infrastructure as code.

## Features

- **Log Processing**: The Lambda function processes incoming log or event data.
- **OpenSearch Integration**: Data is sent to an OpenSearch domain for indexing.
- **Secure Communication**: HTTPS and IAM roles ensure secure communication and access control.
- **Scalable**: The architecture is designed to handle varying loads.

## Environment Variables

The Lambda function requires the following environment variables to be set:

- `OPENSEARCH_ENDPOINT`: The endpoint URL for the OpenSearch domain.
- `OPENSEARCH_USER`: The username for OpenSearch authentication.
- `OPENSEARCH_PASSWORD`: The password for OpenSearch authentication.

These variables are dynamically injected into the Lambda function via Terraform.

## Deployment

### Prerequisites

- Terraform installed on your local machine.
- AWS account with appropriate permissions.
- Python 3.8 runtime for the Lambda function.

