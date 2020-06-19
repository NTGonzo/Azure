from flask import Flask

app = Flask(__name__)                 # creates app instance


@app.route("/")                       # at the end point /
def index():                          # calls method
    return "<h1>Hello Azure!</h1>"    # returns this


if __name__ == "__main__":             # on running python app.py
    app.run(debug=True)                # run flask app, runs on 127.0.0.1:5000, debug while svr active
    