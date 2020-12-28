from MainScores import score_server
from flask import Flask

app = Flask(__name__)


@app.route('/')
def initial_endpoint():
    return score_server()


if __name__ == '__main__':
    app.run()
