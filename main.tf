# Module to call the S3 module (main.tf) to create a ZIP of the source code and upload it to S3
module "s3_code_upload" {
    source = "./modules/s3"  # Path to the S3 module folder

    # bucket_name = "bucket.name"  # Uncomment this line to use a custom bucket name; otherwise, the default will be used

    source_file = "./src"  # Path to the source file that needs to be zipped and uploaded
    output_path = "firmwarelambda${formatdate("YYYYMMDDHHmmss", timestamp())}.zip"  
    # Dynamically generating the ZIP file name with a timestamp to ensure uniqueness
}


# Module to call the Lambda module (main.tf) to create a Lambda function
module "lambda_code" {
    source = "./modules/lambda"  # Path to the Lambda module folder
    function_name = "firmware_lambda5"  # Name of the Lambda function to be created
    s3_bucket = "s3amal"  # The S3 bucket where the ZIP file is stored
    s3_key = module.s3_code_upload.output_path  # Refers to the ZIP file created by the S3 module
    runtime = "python3.9"  # Runtime environment for the Lambda function
    handler = "lambda_code.handler"  # The handler function in the Lambda code
    depends_on = [ module.s3_code_upload ]
}

