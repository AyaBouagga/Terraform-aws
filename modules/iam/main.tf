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

# AWS Caller Identity (for dynamic account reference)
data "aws_caller_identity" "current" {}

# IAM Policy for Lambda to access OpenSearch
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

# Attach IAM policy to Lambda execution role
resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  policy_arn = aws_iam_policy.lambda_policy.arn
  role       = aws_iam_role.lambda_role.name
}

# Output the Lambda Role ARN
output "lambda_role_arn" {
  value = aws_iam_role.lambda_role.arn
}