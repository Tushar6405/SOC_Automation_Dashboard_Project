import boto3

sns = boto3.client('sns', region_name='ap-south-1')

sns.publish(
    TopicArn='YOUR_SNS_ARN',
    Message='Critical SOC Alert Detected',
    Subject='SOC Alert'
)