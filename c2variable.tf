#AWS Region
variable "aws_region" {
    description = "Region in which AWS resources will be created"
    type = string
    default = "us-east-2"
  
}

# Environment Variable
variable "environment" {
  description = "Environment Variable used as a prefix"
  type = string
  default = "dev"
}