import pymysql
import os
from dotenv import load_dotenv
from schemas.post import Post

load_dotenv()

def get_post():
    with pymysql.connect(host=os.getenv('POST_HOST'),
                         user=os.getenv('AWS_USER'),
                         password=os.getenv('AWS_PASSWORD'),
                         db=os.getenv('POST_DB'),
                         charset='utf8') as connection:

        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
        SELECT     
            post_id,
            user_id, 
            content
        FROM
            `posts`
        '''

        cursor.execute(SQL)

        data = cursor.fetchall()

        data = [Post(post_id=row['post_id'], user_id=row['user_id'], content=row['content']) for row in data]

    return data