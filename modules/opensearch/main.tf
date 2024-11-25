resource "aws_opensearch_domain" "logs" {
  domain_name    = var.opensearch_domain_name
  engine_version = "OpenSearch_1.3"

  ebs_options {
    ebs_enabled = true
    volume_type = "gp2"
    volume_size = 10
  }

  node_to_node_encryption {
    enabled = true
  }

  encrypt_at_rest {
    enabled = true
  }

  cluster_config {
    instance_type  = "t3.small.search"
    instance_count = 1
  }

  advanced_security_options {
    enabled                        = true
    internal_user_database_enabled = true

    master_user_options {
      master_user_name     = var.opensearch_user
      master_user_password = var.opensearch_password
    }
  }

  domain_endpoint_options {
    enforce_https = true
  }
}

output "opensearch_endpoint" {
  value = aws_opensearch_domain.logs.endpoint
}