resource "aws_lambda_function" "lambda" {
  function_name = var.lambda_function_name
  role          = var.lambda_role_arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  filename      = var.filename
  timeout       = 10
  memory_size   = 128

  environment {
    variables = {
      OPENSEARCH_ENDPOINT = var.opensearch_endpoint 
      OPENSEARCH_USER     = var.opensearch_user
      OPENSEARCH_PASSWORD = var.opensearch_password
    }
  }

  source_code_hash = filebase64sha256(var.filename)
}