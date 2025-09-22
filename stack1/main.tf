#   stack1\main.tf

provider "aws" {
  region = "us-west-1"  # Changed to match N. California
}

data "aws_vpc" "existing" {
  id = "vpc-0c3ced4659eeb809d"
}

data "aws_subnet" "subnet1" {
  id = "subnet-010b2442ec44a11e6"
}

data "aws_subnet" "subnet2" {
  id = "subnet-075a2c28e34faccf6"
}

module "aurora_serverless" {
  source = "../modules/database"

  cluster_identifier = "my-aurora-serverless"
  vpc_id             = data.aws_vpc.existing.id
  subnet_ids         = [data.aws_subnet.subnet1.id, data.aws_subnet.subnet2.id]

  # Optionally override other defaults
  database_name         = "myapp"
  master_username       = "dbadmin"
  max_capacity          = 1
  min_capacity          = 0.5
  allowed_cidr_blocks   = ["172.31.0.0/16", "0.0.0.0/0"]  # Match existing VPC CIDR
}

data "aws_caller_identity" "current" {}

locals {
  bucket_name = "bedrock-kb-${data.aws_caller_identity.current.account_id}"
}

module "s3_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "~> 3.0"

  bucket = local.bucket_name
  acl    = "private"
  force_destroy = true

  control_object_ownership = true
  object_ownership         = "BucketOwnerPreferred"

  versioning = {
    enabled = true
  }

  server_side_encryption_configuration = {
    rule = {
      apply_server_side_encryption_by_default = {
        sse_algorithm = "AES256"
      }
    }
  }

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}


