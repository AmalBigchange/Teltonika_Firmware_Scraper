variable "function_name" {
  description = "name of the lamabda function"
  type = string
}
variable "s3_bucket" {
  description = "name of the s3 bucket"
  type = string
}
variable "s3_key" {
  description = "name of the s3 key"
  type = string
}
variable "handler" {
  description = "name of the lamabda handler"
  type = string
}
variable "runtime" {
  description = "runtime"
  type = string
}
variable "role" {
  description = "IAM Role"
  type = string
  default = "arn:aws:iam::471989956476:role/firmware_lambda"
}