import json
import time
import constonant as constant
import datetime
from datetime import timedelta
import requests
# import pyarrow
import boto3
import pandas as pd
from pandas import DataFrame
from io import BytesIO
from io import StringIO
from json import dumps
#from datetime import datetime as dt
bucket = 'mugiapi' # already created on S3
client = boto3.client('ssm')
sns = boto3.client("sns", region_name="eu-north-1")
ssm = boto3.client("ssm", region_name="eu-north-1")
s3_resource = boto3.resource('s3')
url = ssm.get_parameter(Name=constant.urlapi, WithDecryption=True)["Parameter"]["Value"]
#url = "https://results.us.securityeducation.com/api/reporting/v0.1.0/phishing"
s3_prefix = "result/csvfiles"
def get_datetime():
    dt = datetime.datetime.now()
    return dt.strftime("%Y%m%d"), dt.strftime("%H:%M:%S")
datestr, timestr = get_datetime()
fname = f"data_api_mugiapi_{datestr}_{timestr}.csv"
file_prefix = "/".join([s3_prefix, fname])
def send_sns_success():
    success_sns_arn = ssm.get_parameter(Name=constant.SUCCESSNOTIFICATION, WithDecryption=True)["Parameter"]["Value"]
    component_name = constant.COMPONENT_NAME
    env = ssm.get_parameter(Name=constant.ENVIRONMENT, WithDecryption=True)['Parameter']['Value']
    success_msg = constant.SUCCESS_MSG
    sns_message = (f"{component_name} :  {success_msg}")
    print(sns_message, 'text')
    succ_response = sns.publish(TargetArn=success_sns_arn,Message=json.dumps({'default': json.dumps(sns_message)}),
        Subject= env + " : " + component_name,MessageStructure="json")
    return succ_response
def send_error_sns():
    error_sns_arn = ssm.get_parameter(Name=constant.ERRORNOTIFICATION)["Parameter"]["Value"]
    env = ssm.get_parameter(Name=constant.ENVIRONMENT, WithDecryption=True)['Parameter']['Value']
    error_message=constant.ERROR_MSG
    component_name = constant.COMPONENT_NAME
    sns_message = (f"{component_name} : {error_message}")
    err_response = sns.publish(TargetArn=error_sns_arn,Message=json.dumps({'default': json.dumps(sns_message)}),    Subject=env + " : " + component_name,
        MessageStructure="json")
    return err_response
    send_sns_success()
    
try:
    r = requests.get(url)
    while r.status_code == 403:
        print("The URL is not hit")
        time.sleep(30)
	    
    if r.status_code != 403:
        print("the URL is HIT ")
        d = r.json()
        df = pd.DataFrame(d)
        df.rename(columns={'body':'decription'},inplace=True)
        print(df)
        csv_buffer = StringIO()  # Fixed the parentheses here
        df.to_csv(csv_buffer)
        s3_resource.Object(bucket, file_prefix).put(Body=csv_buffer.getvalue())
        print("CSV written")
      
except Exception as e:
    # TODO: write code...
    print('error',str(e))
    

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }