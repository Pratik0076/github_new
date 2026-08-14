from flask import Flask, jsonify , render_template
from data import data

app = Flask(__name__)


@app.route('/api')
def api():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
