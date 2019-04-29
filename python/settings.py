
from dotenv import load_dotenv
load_dotenv(verbose=True)


# check .env properties
import os
print (os.getenv("REGION"))
print (os.getenv("ACCOUNTID"))
print (os.getenv("IDENTITYPOOLID"))



