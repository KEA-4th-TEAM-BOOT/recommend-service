import os
import requests
from dotenv import load_dotenv
from typing import List
from models.post import Post

load_dotenv()

def get_recommend_post(post_ids: List[int]) -> List[Post]:
    api_url = os.getenv("POST_URL")
    posts = []
    for post_id in post_ids:
        response = requests.get(f'{api_url}/{post_id}')
        if response.status_code == 200:
            json_response = response.json()
            if json_response['code'] == 200:
                data = json_response['data']
                post = Post(
                    id=data['id'],
                    userLink=data['userLink'],
                    personalPostId=data['personalPostId'],
                    postVoiceFileUrl=data['postVoiceFileUrl'],
                    categoryId=data['categoryId'],
                    subCategoryId=data['subCategoryId'],
                    subject=data['subject'],
                    title=data['title'],
                    content=data['content'],
                    thumbnail=data['thumbnail'],
                    thumbnailImageUrl=data['thumbnailImageUrl'],
                    accessibility=data['accessibility'],
                    hitCnt=data['hitCnt'],
                    likeCnt=data['likeCnt'],
                    createdTime=data['createdTime'],
                    comments=data['comments']
                )
                posts.append(post)
            else:
                raise Exception(f"API Error: {json_response['msg']}")
        else:
            raise Exception(f"HTTP Error: {response.status_code}")
    return posts

