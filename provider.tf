provider "aws" {
  region = "us-east-1"
  
  # Assuming the IAM Role using the ARN of the role
  assume_role {
    role_arn     = "arn:aws:iam::216989124908:role/terraform-role"
    session_name = "terraform-session"
  }
}