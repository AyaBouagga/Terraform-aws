import os

# Define the directory structure and file contents
project_structure = {
    # Root-level files
    "main.tf": """
module "iam" {
  source = "./modules/iam"
}

module "opensearch" {
  source = "./modules/opensearch"
}

module "lambda" {
  source              = "./modules/lambda"
  lambda_function_name = var.lambda_function_name
  lambda_role_arn      = module.iam.lambda_role_arn
  filename             = var.lambda_code_file
}
    """,

    "variables.tf": """
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
    """,

    "outputs.tf": """
output "opensearch_endpoint" {
  value = module.opensearch.opensearch_endpoint
}

output "lambda_function_name" {
  value = module.lambda.lambda_function_name
}
    """,

    "terraform.tfvars": """
aws_region             = "us-east-1"
lambda_function_name   = "log-processor"
lambda_code_file       = "function.zip"
opensearch_domain_name = "logs-domain"
    """,

    "provider.tf": """
provider "aws" {
  region = var.aws_region
}
    """,

    # Lambda module files
    "modules/lambda/main.tf": """
resource "aws_lambda_function" "lambda" {
  function_name    = var.lambda_function_name
  runtime          = "python3.8"
  handler          = "lambda_function.lambda_handler"
  role             = var.lambda_role_arn
  filename         = var.filename
  source_code_hash = filebase64sha256(var.filename)
}

output "lambda_function_name" {
  value = aws_lambda_function.lambda.function_name
}
    """,

    # **Adding the `variables.tf` file for Lambda module**
    "modules/lambda/variables.tf": """
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
    """,  # <- This line starts the `modules/lambda/variables.tf` definition (*)

    # IAM module files
    "modules/iam/main.tf": """
resource "aws_iam_role" "lambda_role" {
  name = "lambda-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_policy" "lambda_policy" {
  name        = "lambda-opensearch-policy"
  description = "Policy to allow Lambda to access OpenSearch"
  policy      = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action   = ["es:ESHttpPut", "es:ESHttpPost", "es:ESHttpGet", "es:ESHttpHead"]
        Effect   = "Allow"
        Resource = "arn:aws:es:${var.aws_region}:${data.aws_caller_identity.current.account_id}:domain/${var.opensearch_domain_name}/*"
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  policy_arn = aws_iam_policy.lambda_policy.arn
  role       = aws_iam_role.lambda_role.name
}

output "lambda_role_arn" {
  value = aws_iam_role.lambda_role.arn
}
    """,

    "modules/iam/variables.tf": """
variable "aws_region" {
  description = "The AWS region"
  type        = string
}

variable "opensearch_domain_name" {
  description = "The OpenSearch domain name"
  type        = string
}
    """,

    # OpenSearch module files
    "modules/opensearch/main.tf": """
resource "aws_opensearch_domain" "logs" {
  domain_name           = var.opensearch_domain_name
  elasticsearch_version = "7.10"

  node_to_node_encryption {
    enabled = true
  }

  encrypt_at_rest {
    enabled = true
  }

  cluster_config {
    instance_type = "t2.small.search"
    instance_count = 1
  }
}

output "opensearch_endpoint" {
  value = aws_opensearch_domain.logs.endpoint
}
    """,

    "modules/opensearch/variables.tf": """
variable "opensearch_domain_name" {
  description = "The OpenSearch domain name"
  type        = string
}
    """
}

# Function to create the directory structure and write files
def create_terraform_project():
    for path, content in project_structure.items():
        # Create directories if they don't exist
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Write content to the file
        with open(path, "w") as file:
            file.write(content.strip() + "\n")

# Run the function to create the project
if __name__ == "__main__":
    create_terraform_project()
    print("Terraform project structure created successfully!")