from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    response = render_template('index.html')
    return response

@app.route("/cheatsheet")
def cheatsheet():
    response = render_template('cheatsheet.html')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)