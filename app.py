import os
from fastapi import FastAPI, Header
from google.cloud import bigquery
from google.oauth2.service_account import Credentials
from fastapi.middleware.cors import CORSMiddleware
from authcheck import auth_check
import base64
import json


creds_base64 = os.environ.get("GOOGLE_CREDENTIALS_BASE64")
creds_json_str = base64.b64decode(creds_base64).decode("utf-8")
creds_info = json.loads(creds_json_str)
creds = Credentials.from_service_account_info(creds_info)
client = bigquery.Client(credentials=creds)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods or be specific e.g., ["GET", "POST"]
    allow_headers=["*"],  # Allow all headers or be specific e.g., ["Content-Type"]
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to hushh's LV Card API"}



@app.get("/PII/")
async def get_PII(id: str = Header(None), authentication: str = Header(None)):
    """
    Use this endpoint to get PII information!

    Test Value for id : test@hush1one.com

    Test Value for authorization token : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
    """

    # Checking for authentication
    valid_auth = auth_check(authentication)
    if valid_auth.get("status") != 1:
        return valid_auth

    sql_query = f"""
    SELECT * FROM hushone-app.lvmh_demo.PII_data WHERE email = "{id}"
    """

    try:
        query_job = client.query(sql_query)
        results = [dict(row) for row in query_job]

        if not results:
            return {"message": f"No information found for the specified ID '{id}'."}
        else:
            return results
    
    except:
        return {"message": f"An unexpected error occured for the specified ID '{id}'."}

@app.get("/fashion_purchase_history/")
async def get_fashion_purchase_history(id: str = Header(None), authentication: str = Header(None)):
    """
    Use this endpoint to get purchase history of the user!

    Test Value for id : test@hush1one.com

    Test Value for authorization token : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
    """

    # Checking for authentication
    valid_auth = auth_check(authentication)
    if valid_auth.get("status") != 1:
        return valid_auth

    sql_query = f"""
    SELECT * FROM hushone-app.lvmh_demo.purchase_history_data WHERE email = "{id}"
    """

    try:
        query_job = client.query(sql_query)
        results = [dict(row) for row in query_job]

        if not results:
            return {"message": f"No information found for the specified ID '{id}'."}
        else:
            return results
    
    except:
        return {"message": f"An unexpected error occured for the specified ID '{id}'."}
    
@app.get("/all_transactions/")
async def get_all_transactions(id: str = Header(None), authentication: str = Header(None)):
    """
    Use this endpoint to get transaction history of a user!

    Test Value for id : test@hush1one.com

    Test Value for authorization token : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
    """

    # Checking for authentication
    valid_auth = auth_check(authentication)
    if valid_auth.get("status") != 1:
        return valid_auth

    sql_query = f"""
    SELECT * FROM hushone-app.lvmh_demo.transactions_data WHERE email = "{id}"
    """

    try:
        query_job = client.query(sql_query)
        results = [dict(row) for row in query_job]

        if not results:
            return {"message": f"No account information found for the specified ID '{id}'."}
        else: 
            return results
        
    except:
        return {"message": f"An unexpected error occured for the specified ID '{id}'."}
    
@app.get("/travel_information/")
async def get_travel_information(id: str = Header(None), authentication: str = Header(None)):
    """
    Use this endpoint to get travel information of a user!

    Test Value for id : test@hush1one.com

    Test Value for authorization token : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
    """

    # Checking for authentication
    valid_auth = auth_check(authentication)
    if valid_auth.get("status") != 1:
        return valid_auth

    sql_query = f"""
    SELECT * FROM hushone-app.lvmh_demo.travel_data WHERE email = "{id}"
    """

    try:
        query_job = client.query(sql_query)
        results = [dict(row) for row in query_job]

        if not results:
            return {"message": f"No account information found for the specified ID '{id}'."}
        else: 
            return results
        
    except:
        return {"message": f"An unexpected error occured for the specified ID '{id}'."}
    
@app.get("/health/")
async def get_health_preferences(id: str = Header(None), authentication: str = Header(None)):
    """
    Use this endpoint to get health preferences of a user!

    Test Value for id : test@hush1one.com

    Test Value for authorization token : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
    """

    if id == 'test@hush1one.com':
        id = 'test@hushh1one.com'
    # Checking for authentication
    valid_auth = auth_check(authentication)
    if valid_auth.get("status") != 1:
        return valid_auth

    sql_query = f"""
    SELECT * FROM hushone-app.lvmh_demo.health_data WHERE email = "{id}"
    """

    try:
        query_job = client.query(sql_query)
        results = [dict(row) for row in query_job]

        if not results:
            return {"message": f"No information found for the specified ID '{id}'."}
        else:
            return results
    
    except:
        return {"message": f"An unexpected error occured for the specified ID '{id}'."}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
