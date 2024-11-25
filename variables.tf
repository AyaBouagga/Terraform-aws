variable "aws_region" {
  description = "The AWS region"
  type        = string
  default     = "us-east-1"
}

variable "lambda_function_name" {
  description = "The name of the Lambda function"
  type        = string
  default     = "log-processor"
}

variable "lambda_code_file" {
  description = "The path to the Lambda function zip file"
  type        = string
  default     = "function.zip"
}

variable "opensearch_domain_name" {
  description = "The name of the OpenSearch domain"
  type        = string
  default     = "logs-domain"
}


variable "opensearch_user" {
  description = "The username for OpenSearch basic authentication"
  default     = "admin"
}

variable "opensearch_password" {
  description = "The password for OpenSearch basic authentication"
  default     = "Admin123!"
}