class PostDB:
    def __init__(self, conn):
        self.conn = conn

    def getPosts(self):
        return self.conn.find()

    def createPost(self, post):
        self.conn.insert({'post':post})