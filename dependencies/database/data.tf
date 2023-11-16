terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
}

data "aws_db_instance" "db" {
    tags = {
        name = "friendscapstonerds"
        proj_name = "friends-capstone"
    }
}

output "rds_address" {
    value = data.aws_db_instance.db.address
}

output "rds_name" {
    value = data.aws_db_instance.db.db_name
}


data "template_file" "db_template" {
  template = file("${path.module}/../../.env.db")
  vars = {
    ENDPOINT = data.aws_db_instance.db.address
    DBNAME = data.aws_db_instance.db.db_name
  }
}


resource "local_file" "pycode" {
  content  = data.template_file.db_template.rendered
  filename = "${path.module}/../../.env.db.out"
}