
import boto3
#boto.set_stream_logger('foo')
import json
import os

# load configurations
from dotenv import load_dotenv
load_dotenv(verbose=True)
region= os.getenv("REGION")
accountid = os.getenv("ACCOUNTID")
identitypoolid = os.getenv("IDENTITYPOOLID")
print ("region: "+region)
print ("account: "+accountid)
print ("identity pool id: "+identitypoolid)

client = boto3.client('cognito-identity',region)
resp =  client.get_id(AccountId=accountid,IdentityPoolId=identitypoolid)
print ("\nIdentity ID: %s"%(resp['IdentityId']))
print ("\nRequest ID: %s"%(resp['ResponseMetadata']['RequestId']))
resp = client.get_open_id_token(IdentityId=resp['IdentityId'])
token = resp['Token']
print ("\nToken: %s"%(token))
print ("\nIdentity ID: %s"%(resp['IdentityId']))
resp = client.get_credentials_for_identity(IdentityId=resp['IdentityId'])
secretKey = resp['Credentials']['SecretKey']
accessKey = resp['Credentials']['AccessKeyId']
print ("\nSecretKey: %s"%(secretKey))
print ("\nAccessKey ID: %s"%(accessKey))
print (resp)
