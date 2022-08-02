terraform {
  cloud {
    organization = "Minha"

    workspaces {
      name = "Desafio_Audaces"
    }
  }
}

provider "aws" {
    region = "us-east-1"
}