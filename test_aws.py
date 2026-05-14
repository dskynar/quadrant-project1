import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def verify_aws_connection():
    try:
        # Boto3 will automatically use the AWS_PROFILE environment variable 
        # or the [default] profile in your ~/.aws/config
        sts = boto3.client('sts')
        
        # This call returns details about the IAM user/role being used
        identity = sts.get_caller_identity()
        
        print("✅ AWS Connection Successful!")
        print(f"   Account: {identity['Account']}")
        print(f"   User ID: {identity['UserId']}")
        print(f"   ARN:     {identity['Arn']}")

    except NoCredentialsError:
        print("❌ Error: No AWS credentials found. Did you run 'aws sso login'?")
    except ClientError as e:
        print(f"❌ AWS Client Error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    verify_aws_connection()
