from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is running successfully Gauri!"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=5000)

