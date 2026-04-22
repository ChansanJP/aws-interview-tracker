from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>AWS Interview Tracker</h1><p>Your app is alive.</p>"

if __name__ == "__main__":
    app.run(debug=True)
