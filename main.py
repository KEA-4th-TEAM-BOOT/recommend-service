import os
import uvicorn
import csv
from fastapi import FastAPI

import pymongo
from bson import ObjectId

# mongodb connection 연결
connection = pymongo.MongoClient("mongodb://root:1111@172.16.226.46:27017/")

# 데이터베이스를 찾는다.
database = connection["recommend_test"]

# 데이터베이스에서 컬렉션을 찾는다.
collection = database["post"]

app = FastAPI()

port = int(os.environ.get("RECOMMEND_PORT", 8001))

print(collection.find())
@app.get("/")
async def root():
    result = []
    cursor = collection.find()
    for document in cursor:
        # ObjectId를 문자열로 변환하여 직렬화
        document["_id"] = str(document["_id"])
        result.append(document)

    fieldnames = ['_id', 'content']

    f = open("data.csv", "w")
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(result)

    f.close()

    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)