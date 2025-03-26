## variables.tf
variable "aws_region" { default = "us-east-1" }
variable "vpc_cidr" { default = "10.0.0.0/16" }

variable "public_subnet_cidrs" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}


variable "private_subnet_cidrs" { 
  type = list(string)
  default = ["10.0.3.0/24", "10.0.4.0/24"] 
}

variable "eks_cluster_name" { default = "my-cluster" }
variable "node_instance_type" { default = "t3.medium" }


variable "db_instance_identifier" {
  description = "RDS instance identifier"
  type        = string
  default     = "my-postgres-db"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "mydatabase"
}

variable "db_username" {
  description = "Master username for PostgreSQL"
  type        = string
  default     = "admin"
}

variable "db_password" {
  description = "Master password for PostgreSQL"
  type        = string
  sensitive   = true
}

variable "db_instance_class" {
  description = "RDS instance type"
  type        = string
  default     = "db.t3.micro"
}

variable "db_allocated_storage" {
  description = "Storage size (GB)"
  type        = number
  default     = 20
}

variable "db_engine_version" {
  description = "PostgreSQL engine version"
  type        = string
  default     = "15.3"
}

variable "db_subnet_group_name" {
  description = "RDS subnet group name"
  type        = string
  default     = "my-db-subnet-group"
}
