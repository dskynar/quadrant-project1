terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0" # Using the latest 2026 provider version
    }
  }
}

provider "aws" {
  region = "eu-central-1"
  # Note: We omit 'profile' here because you've exported AWS_PROFILE.
  # This makes your code more portable for others!
}
