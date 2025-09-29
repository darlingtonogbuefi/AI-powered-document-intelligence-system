variable "aws_region" {
  type    = string
  default = "us-west-2"
}

variable "knowledge_base_name" {
  type = string
}

variable "knowledge_base_description" {
  type = string
}

variable "aurora_arn" {
  type = string
  description = "ARN of the Aurora Serverless cluster" # TODO Update with output from stack1
}

variable "aurora_db_name" {
  type = string
}

variable "aurora_endpoint" {
  type = string
  description = "Endpoint of Aurora Serverless cluster" # TODO Update with output from stack1
}

variable "aurora_table_name" {
  type = string
}

variable "aurora_primary_key_field" {
  type = string
}

variable "aurora_metadata_field" {
  type = string
}

variable "aurora_text_field" {
  type = string
}

variable "aurora_verctor_field" {
  type = string
}

variable "aurora_username" {
  type = string
}

variable "aurora_secret_arn" {
  type = string
  description = "ARN of the Secrets Manager secret for DB credentials" # TODO Update with output from stack1
}

variable "s3_bucket_arn" {
  type = string
  description = "ARN of the S3 bucket" # TODO Update with output from stack1
}
