from models.posts_db import PostsDB

class PostsService:
    def __init__(self):
        self.posts_db = PostsDB()

    def get_posts(self):
        return self.posts_db.get_posts()
    
    def new_post(self, post):
        return self.posts_db.new_post(post=post)

    def update_post(self, post):
        return self.posts_db.update_post(post=post)

    def get_one(self, index):
        return self.posts_db.get_one(id = index)

    def delete_post(self, index):
       return self.posts_db.delete_post(id = index)