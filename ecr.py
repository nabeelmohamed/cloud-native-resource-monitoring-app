import boto3

ecr_client=boto3.client('ecr')
repository_name="cloud_native_repo"

response=ecr_client.create_repository(repositoryName=repository_name)

repository_uri=response['repository']['repositoryUri']

print(repository_uri)
print("ECR repository created successfully")