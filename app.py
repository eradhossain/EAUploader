from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello <a href="https://t.me/EaUploaderBot">@EaUploaderBot</a>'


if __name__ == "__main__":
    app.run()
