from flask import Flask
 
app = Flask(__name__,)

@app.route("/")
def Welcome():
    return 'Welcome!'

@app.route("/<username>")
def welcome_user(username):
    return 'Welcome ' + username + '!'

if __name__ == "__main__":
    app.run(debug=True)