from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hi, I am Nisha Vishwakarma</h1>
    <h3>From Muzaffarnagar, UP</h3>
    <p>I am learning Python | Flask | GitHub</p>
    <p>My Portfolio is LIVE!</p>
    <p>Check my projects on GitHub</p>
    """

if __name__ == "__main__":
    app.run()
