terraform {
  required_version = ">= 1.0"  # Specify the minimum Terraform version

  required_providers {
    aws = {
      source  = "hashicorp/aws"  # Specifies the Terraform Registry as the source
      version = "~> 4.0"         # Use a version constraint to ensure compatibility
    }
  }
}

provider "aws" {
  region  = "eu-west-2"  # Default region; this can be overridden in variable definitions
 
}