from flask import Flask, request, render_template
# from flask import url_for 

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
    if request.method == 'POST':
        return 'In here via POST request.'
    else:
        return 'In here via GET request.'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def application_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    # with app.test_request_context():
    #     print url_for('welcome_user', username='Sarah Connor')
    app.run(debug=True)