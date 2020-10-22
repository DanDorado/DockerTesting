from flask import Flask
import random
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    user = os.getenv["$USER"]
    return("Hello, folks. My random number is " +
    str(random_number(1000)) + ". \nThe username pulled from .env is " + str(user) + ".\n")

def random_number(max):
    return(random.randint(100,max))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=1000, debug = True)