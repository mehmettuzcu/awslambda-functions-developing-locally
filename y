version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "ingest"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-1ugblzamduso5"
s3_prefix = "ingest"
region = "eu-west-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
image_repositories = []

[default]
[default.deploy]
[default.deploy.parameters]
stack_name = "ingest"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-1ugblzamduso5"
s3_prefix = "ingest"
region = "eu-west-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
image_repositories = []
