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

# data "aws_lambda_function" "lambda" {
#   function_name = "friends-capstone-notification-lambda"
# }

# data "aws_iam_role" "eventbridgerole" {
#   name = "friends-capstone-notification-eventbridge-role"
#   tags = {
#     name = "friends-capstone-notification-eventbridge-role"
#   }
# }

# output "lambda_arn" {
#     value = data.aws_lambda_function.lambda.arn
# }

# output "eventbridgerole_arn" {
#     value = data.aws_iam_role.eventbridgerole.arn
# }

data "template_file" "lambda_template" {
  template = file("${path.module}/../../.env.lambda")
  vars = {
    LAMBDAARN = "#{LAMBDA_EMAIL_SVC_ARN}#"
    EVENTBRIDGEIAMROLEARN = "#{EVENTBRIDGEROLE_EMAIL_SVC_ARN}#"
  }
}



resource "local_file" "pycode" {
  content  = data.template_file.lambda_template.rendered
  filename = "${path.module}/../../.env.lambda.out"
}

