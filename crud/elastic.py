import os
import requests
from dotenv import load_dotenv
from typing import List
from schemas.post import Post

load_dotenv()

def get_posts() -> List[Post]:
    es_url = os.getenv("ES_URL")
    index = os.getenv("ES_INDEX")
    user = os.getenv("ES_USER")
    password = os.getenv("ES_PASSWORD")
    query = {
        "query": {
            "match_all": {}
        }
    }

    response = requests.get(f"{es_url}/{index}/_search", json=query, auth=(user, password))

    if response.status_code == 200:
        json_response = response.json()
        hits = json_response['hits']['hits']
        posts = [Post(
            post_id=hit['_source']['post_id'],
            user_id=hit['_source']['user_id'],
            content=hit['_source']['content'])
            for hit in hits]
        return posts
    else:
        raise Exception(f"HTTP Error: {response.status_code}, {response.text}")