# Referencing an existing S3 bucket
data "aws_s3_bucket" "existing_bucket" {
  bucket = var.bucket_name  # Fetching the bucket name from a variable
}

# Creating a ZIP archive of the source code
data "archive_file" "lambda_zip" {
  type        = "zip"         # Defining the type of archive (ZIP in this case)
  source_dir = var.source_file  # Path to the source code file, provided via a variable
  output_path = var.output_path  # Naming the output ZIP file (can be dynamic via a variable)
}

# Uploading the ZIP file to the specified S3 bucket
resource "aws_s3_object" "lambda_code" {
  bucket = data.aws_s3_bucket.existing_bucket.bucket  # Referring to the existing S3 bucket
  key    = var.output_path  # Setting the S3 object key to match the ZIP file name
  source = data.archive_file.lambda_zip.output_path  # Providing the path of the ZIP file generated in the archive step
}