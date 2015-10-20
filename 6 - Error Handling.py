from flask import Flask, request, jsonify
# from flask import url_for 
# import json

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

@app.route('/methods', methods=['GET', 'POST'])
def methods():
    participants = [{"name":"Ali", "age":20},
                    {"name":"Ruth", "age":24},
                    {"name":"Andrew", "age":22},
                    {"name":"Pat", "age":25}]
    if request.method == 'POST':
        return 'In here via POST request.'
    else:
        return jsonify(participants=participants)

@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found!'

@app.errorhandler(500)
def application_error(e):
    return 'Server Error!'

if __name__ == "__main__":
    # with app.test_request_context():
    #     print url_for('welcome_user', username='Sarah Connor')
    app.run(debug=True)