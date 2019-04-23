import boto3

#TODO
def lambda_handler(event, context):
    client = boto3.client('ecs')
    response = client.run_task(
        cluster='test-cluster',
        taskDefinition='test-task-definition',
        launchType = 'FARGATE',
        count = 1,
        startedBy='lambdaFunction-start',
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': ['subnet-###############'], 
                'securityGroups': ['sg-#############'],
                'assignPublicIp': 'ENABLED'
            }
        }
    )
    clientDB = boto3.client('dynamodb')
    responseDB = clientDB.put_item(
        TableName='TaskList',
        Item={
            'TaskName':{
                'S': str(response["tasks"][0]['taskArn']),
                }
        }
        )
    return str(responseDB)
