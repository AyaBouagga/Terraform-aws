module "iam" {
  source = "./modules/iam"

  aws_region             = var.aws_region
  opensearch_domain_name = var.opensearch_domain_name
}

module "opensearch" {
  source = "./modules/opensearch"
  aws_region = var.aws_region
  opensearch_domain_name = var.opensearch_domain_name

}

module "lambda" {
  source              = "./modules/lambda"
  lambda_function_name = var.lambda_function_name
  lambda_role_arn = module.iam.lambda_role_arn
  filename= var.lambda_code_file
  opensearch_endpoint = module.opensearch.opensearch_endpoint  # Passing OpenSearch endpoint
}