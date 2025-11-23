variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-2"
}

variable "app_name" {
  description = "Name of the application (used for tagging and naming)"
  type        = string
  default     = "my-api"
}

variable "container_port" {
  description = "Port the container listens on"
  type        = number
  default     = 8080
}
