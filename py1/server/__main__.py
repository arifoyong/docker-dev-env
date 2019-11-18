from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def main():
    return "=== Response from flask server ==="


if __name__ == "__main__":
    port = os.environ["PORT"] if "PORT" in os.environ else 9000
    app.run(host="0.0.0.0", port=port)
