from flask import Flask, request
import os
import openai
from twilio_service import send_sms
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return "Server is up"

@app.route("/greet")
def hello():
    return "Hello from the other side"

@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user(username):
    if request.method == 'GET':
        return 'Username: %s' % username

    if request.method == 'POST':
        return {"username": username}

@app.route('/post/<int:post_id>')
def show_post(post_id):
  return str(post_id)

@app.route("/upload-audio", methods=['POST'])
@cross_origin()
def handle_upload():
    print("incoming request")
    audio_file = request.files["audio_message"]
    audio_file.save("./message.m4a")
    audio = open("./message.m4a", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio)
    print(transcript)

    send_sms("+919153459675", transcript.text)

    return transcript
