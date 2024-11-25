variable "lambda_function_name" {
  description = "The name of the Lambda function"
  type        = string
}

variable "lambda_role_arn" {
  description = "The ARN of the IAM role for the Lambda function"
  type        = string
}

variable "filename" {
  description = "The path to the Lambda function code zip file"
  type        = string
}
variable "opensearch_endpoint" {
  description = "The endpoint for OpenSearch"
  type        = string
}

variable "opensearch_user" {
  description = "The username for OpenSearch basic authentication"
  default     = "admin"
}

variable "opensearch_password" {
  description = "The password for OpenSearch basic authentication"
  default     = "Admin123!"
}