class UsersDB:
    def __init__(self, conn):
        self.conn = conn
        self.uname = ""

    def getUser(self, username, password):
        account =  self.conn.find_one({'account': { 'username': username, 'password': password }})
        self.uname = account['account']['username']

        return self.uname

    def signupUser(self, username, password):
        self.conn.insert(
        	{
        		'account': {
        			'username': username,
        			'password': password
        		},

        		'posts': [

        		]
        	}
        )

    def getPosts(self):
    	account = self.conn.find_one({'account': { 'username': self.uname }})

        print self.uname + " username"