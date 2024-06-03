from bs4 import BeautifulSoup
from typing import List
from schemas.post import Post

def clean_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def filter_user(posts, user_id: int) -> List[Post]:
    filtered_data = [post for post in posts if post.user_id != user_id]
    return filtered_data

def clean_data(posts: List[Post], user_id: int) -> List[Post]:
    posts = filter_user(posts, user_id)
    for post in posts:
        post.content = clean_html(post.content)
    return posts