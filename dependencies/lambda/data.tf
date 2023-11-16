terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

data "aws_lambda_function" "lambda" {
  function_name = "friends-capstone-notification-lambda"
}

output "lambda_arn" {
    value = data.aws_lambda_function.lambda.arn
}

data "template_file" "lambda_template" {
  template = file("${path.module}/../../.env.lambda")
  vars = {
    LAMBDAARN = data.aws_lambda_function.lambda.arn
  }
}


resource "local_file" "pycode" {
  content  = data.template_file.lambda_template.rendered
  filename = "${path.module}/../../.env.lambda.out"
}
