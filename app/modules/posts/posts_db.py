class PostDB:
    def __init__(self, conn):
        self.conn = conn

    def getPosts(self, username):
        return self.conn.find()

    def createPost(self, post, username):
        self.conn.insert({'post':post})