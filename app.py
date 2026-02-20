from flask import Flask, render_template, request
import phonenumbers
from bot import send_notification

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        name = request.form.get('userName')
        phone_number = request.form.get('userPhone')
        send_notification(name, phone_number)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)