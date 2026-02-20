from flask import Flask, render_template, request
import phonenumbers
app = Flask(__name__)


@app.route('/', )
def main_page():
    return render_template('index.html')


@app.route('/send_lead', methods=['POST'])
def send_lead():
    name = request.form.get('userName')
    tel = request.form.get('userPhone')
    parsed_tel = phonenumbers.parse(tel)
    if phonenumbers.is_valid_number(parsed_tel):


if __name__ == '__main__':
    app.run(debug=True)