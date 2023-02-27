## import libraries
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

## build the condition for using url_for
@app.route("/postman_test2", methods=["POST"]) ## <name> denotes the sub for the condition
def family():  ## function for the condition for determination!!!!
    if (request.method == "POST"):
        name = request.json["name"] 
        if name == "father":
            result = f"My Father's name is Olushola David"
        if name == "mother":
            result = f"My Mothers's name is Felicia Asabi"
        if name == "son":
            result = f"My name is Abwonder"
        return jsonify(result)
    
if __name__=="__main__":
    app.run(host="0.0.0.0")