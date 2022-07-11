#Create VPC Terraform Module

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
    version = "3.14.2.0"

 # VPC Basic Details
  name = var.vpc_name
  cidr = var.vpc_cidr_block
  azs             = var.vpc_availability_zones
  private_subnets = var.vpc_public_subnets
  public_subnets  = var.vpc_private_subnets


# Database Subnets
database_subnets = var.vpc_database_subnets


#   enable_nat_gateway = true
#   enable_vpn_gateway = true

#   tags = {
#     Terraform = "true"
#     Environment = "dev"
#   }
}