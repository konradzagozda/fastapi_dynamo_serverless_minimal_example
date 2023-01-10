import boto3 as boto3
from fastapi import FastAPI
from mangum import Mangum
import os

app = FastAPI()



dynamodb_client = boto3.client('dynamodb')

@app.get("/")
async def root():
    dynamodb_client.put_item(
        TableName='Items', Item={'itemId': {'S': 1}, 'name': {'S': 'item1'}}
    )
    item = dynamodb_client.get_item(
        TableName='Items', Key={'userId': {'S': 1}}
    ).get('Item')

    KEY = os.getenv('KEY')

    return {"message": "Hello World", "KEY": KEY, "itemName": item.get('name').get('S')}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

handler = Mangum(app)
