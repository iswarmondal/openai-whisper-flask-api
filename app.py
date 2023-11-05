from flask import Flask

app = Flask(__name__)

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
def handle_upload():
    if request.method == "POST":
        audio_file = request.files["audio_message"]
        audio_file.save("/var/www/uploads/message.mp4")

        return {"success" : true}
