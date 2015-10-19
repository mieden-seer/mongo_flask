from flask import Flask, url_for
 
app = Flask(__name__,)

@app.route("/")
def Welcome():
    return 'Welcome!'

@app.route("/<username>")
def welcome_user(username):
    return 'Welcome ' + username + '!'

@app.route('/with_int/<int:number>')
def show_number(number):
    return 'We\'re counting with number '+ str(number) +'!'

if __name__ == "__main__":
    with app.test_request_context():
        print url_for('welcome_user', username='Sarah Connor')
    app.run(debug=True)