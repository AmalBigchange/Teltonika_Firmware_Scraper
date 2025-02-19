#variable holding the bucket name (change the default value to reference another exisiting bucket)
variable "bucket_name" {
  description = "s3 bucket name"
  type = string
  default = "s3amal"
}

#variable holding the source file path
variable "source_file" {
  description = "Path to the source file to be uploaded."
  type        = string
}

variable "output_path" {
  description = "Path to the source file to be uploaded."
  type        = string
}