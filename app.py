from flask import Flask, jsonify, render_template,redirect, url_for
#from api.data import data_connector

from flask import request
from classification_function import classification_func

# app = Flask(__name__, static_url_path='')
app = Flask(__name__)

# serve a dynamic html file from the flask app
@app.route('/', methods=['POST', "GET"])
def index():
    if request.method == "POST":
        review = request.form["feedback"]
        result = classification_func(review)
        if (result == 1):
            res_final = "NEGATIVE REVIEW"
        else:
            res_final = "POSITIVE REVIEW"
        return render_template('html/results.html',res=[res_final,review])
    else:
        return render_template('html/index.html')

@app.route("/results")
def result_page(res):
    return render_template('html/results.html')
    

if __name__ == "__main__":
    app.run(debug=True)