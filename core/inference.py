import os
import json
from dotenv import load_dotenv
from typing import List
from schemas.post import Post
from schemas.user import User
from schemas.similarity import Similarity
from schemas.post_similarity import PostSimilarity
from core.endpoint import query_endpoint_embedding_with_json_payload, transform_output
from core.score import show_embedding_score

load_dotenv()

def request_endpoint(user: User, posts: List[Post]) -> List[Similarity]:
    endpoint_name = os.getenv('RECOMMEND_ENDPOINT')

    user_payload = {
        "inputs": user.user_post
    }

    user_response = query_endpoint_embedding_with_json_payload(
        json.dumps(user_payload).encode("utf-8"), endpoint_name=endpoint_name
    )

    user_emb = transform_output(user_response['Body'])

    similarities = []
    for post in posts:
        post_payload = {
            "inputs": post.content
        }

        query_response = query_endpoint_embedding_with_json_payload(
            json.dumps(post_payload).encode("utf-8"), endpoint_name=endpoint_name
        )
        post_emb = transform_output(query_response['Body'])

        score = show_embedding_score(user_emb, post_emb)

        similarity = Similarity(
            user_id=user.user_id,
            post_id=post.post_id,
            similarity=score.item()
        )
        similarities.append(similarity)

    return similarities

def request_endpoint_post(user_post: Post, posts: List[Post]) -> List[PostSimilarity]:
    endpoint_name = os.getenv('RECOMMEND_ENDPOINT')

    user_payload = {
        "inputs": user_post.content
    }

    user_response = query_endpoint_embedding_with_json_payload(
        json.dumps(user_payload).encode("utf-8"), endpoint_name=endpoint_name
    )

    user_emb = transform_output(user_response['Body'])

    similarities = []
    for post in posts:
        post_payload = {
            "inputs": post.content
        }

        query_response = query_endpoint_embedding_with_json_payload(
            json.dumps(post_payload).encode("utf-8"), endpoint_name=endpoint_name
        )
        post_emb = transform_output(query_response['Body'])

        score = show_embedding_score(user_emb, post_emb)

        similarity = PostSimilarity(
            post1_id=user_post.post_id,
            post2_id=post.post_id,
            similarity=score.item()
        )
        similarities.append(similarity)

    return similarities