import os
import requests
from dotenv import load_dotenv
from schemas.user import User

load_dotenv()

def get_liked_posts(user_id: int) -> str:
    api_url = os.getenv("LIKE_POST_URL")
    params = {
        "userId": user_id,
        "page": 0,
        "size": 5
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        json_response = response.json()
        if json_response['code'] == 200:
            data = json_response['data']
            user_posts = [post['content'] for post in data]
            concatenated_content = ' '.join(user_posts)
            return concatenated_content
        else:
            raise Exception(f"API Error: {json_response['msg']}")
    else:
        raise Exception(f"HTTP Error: {response.status_code}")

def make_user(user_id: int) -> User:
    user_post = get_liked_posts(user_id)
    return User(user_id=user_id, user_post=user_post)

