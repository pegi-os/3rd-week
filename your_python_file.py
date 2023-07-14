from flask import Flask, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def process_number():
    if request.method == "POST":
        number = int(request.form["number"])
        if number < 10:
            result = "Success"
        else:
            result = "Fail"

        with open("data.txt", "a") as file:
            file.write(str(number) + "\n")

        return result
    else:
        return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
