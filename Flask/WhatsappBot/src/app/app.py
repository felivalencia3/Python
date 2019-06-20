import requests
from flask import Flask, render_template, request
from twilio.rest import Client

SID = "AC652c51e939f97d17a00c3105769649d7"
KEY = "df7e3c41ef9a295051542cc50666c3ee"

app = Flask(__name__)
client = Client(SID, KEY)


@app.route('/incoming', methods=['POST'])
def incoming():
    to = request.form['To']
    origin = request.form['Form']
    response = requests.get('https://quota.glitch.me/random')
    text = response.json()
    message = client.messages.create(
        from_=origin,
        body=text,
        to=to
    )
    return str(message.error_code or 200)


if __name__ == "__main__":
    app.run(debug=True)
