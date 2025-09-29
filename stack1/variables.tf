# stack1\variables.tf
# Variables for stack1

variable "vpc_id" {
  description = "The ID of the existing VPC"
  type        = string
}

variable "subnet1_id" {
  description = "The ID of subnet 1"
  type        = string
}

variable "subnet2_id" {
  description = "The ID of subnet 2"
  type        = string
}
