import json
from flask import Flask, request
import os
from services.twilio_service import send_sms, send_bulk_sms
from flask_cors import CORS, cross_origin
from services.openai_service import translate
from contact_numbers import list_of_numbers

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def index():
    return "Server is up"

@app.route("/greet")
def hello():
    return "Hello from the other side"

@app.route("/translate-audio", methods=['POST'])
@cross_origin()
def handle_translation():
    audio_file = request.files["audio_message"]
    audio_file.save("./message.m4a")
    abs_path = os.path.abspath("./message.m4a")
    res=translate(audio_path=abs_path)
    res_json=json.loads(res)

    send_sms("+919153459675", res_json["text"])

    return {"success": "true", "message":"Message sent"}

@app.route("/send-bulk-sms", methods=['POST'])
@cross_origin()
def handle_sending_bulk_sms():
    data = request.get_json()
    message=data["message"]
    send_bulk_sms(numbers_list=list_of_numbers, body=message)
    return {"success": "true", "message": message}
