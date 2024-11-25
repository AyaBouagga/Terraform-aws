variable "opensearch_domain_name" {
  description = "The OpenSearch domain name"
  type        = string
}
variable "aws_region" {
  description = "The AWS region"
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