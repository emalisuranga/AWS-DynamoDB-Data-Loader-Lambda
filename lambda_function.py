import json
import boto3

def lambda_handler(event, context):
    # Initialize the DynamoDB resource
    dynamodb_resource = boto3.resource('dynamodb')
    
    # Specify the table name
    table_name = 'SalesRecruitmentProgressManagement'
    
    try:
        # Get a reference to the DynamoDB table
        table = dynamodb_resource.Table(table_name)
        
        # Assuming the input is a JSON array in the event
        json_array = event['inputJson']
                    
        # Load the JSON array
        # data_array = json.loads(json_array)
        
        # Loop through the array and put each item into DynamoDB
        for item in json_array:
            table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': 'Data stored successfully in DynamoDB.'
        }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json_array
        }
