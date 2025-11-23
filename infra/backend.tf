# infra/backend.tf

terraform {
  backend "s3" {
    bucket = "chariis-terraform-state"
    key    = "global/ecs-api/terraform.tfstate"
    region = "us-east-1"

    dynamodb_table = "chariis-terraform-state-lock"

    encrypt = true
  }
}
