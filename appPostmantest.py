## convert former script to be used with postman (World reknown app for testing API)

from flask import Flask, request, render_template, jsonify   ### all library are needed for this job!!!

app = Flask(__name__)

### home page declaration
@app.route("/")  ## declared to map the function to url
def home_pager():
    return render_template("index.html")  ## index in same directory although subfolderl. ## front end are to provide this!!! both bonus if you are good with html

## Dealing with the math("/")

@app.route("/postman_action", methods= ["POST"]) ## where bond everything to route on url; Also specify how to make the data available!! method == POST
def math_op1():
    if(request.method == "POST"):  ## mean it will not be visible on the url, gotten thru form
       ## all the client side data entry will need to be obtainedbo, both POST and GET can be use to get data
       ## differences is that POST will not be visible on the url, while GET will be!!
        ops = request.json["operation"]  ## operatin is label -- check this on the source page on the url or check the source code index.html
        num1 = int(request.json["num1"])  ## this is the second input label on the page
        num2 = int(request.json["num2"])  ## same use the index.html to get this information
        if ops == "add":
            r = num1 + num2
            result = f'The sum of {num1} and {num2} is:  {r}'
            # return render_template("results.html", result = result)

        if ops == "subtract":
            r = num1 - num2
            result = f'The subtraction of {num2} from {num1} is:  {r}'
            # return render_template("results.html", result = result)

        if ops == "<multiply":
            r = num1 * num2
            result = f'The multiplication of {num1} and {num2} is:  {r}'
            # return render_template("results.html", result = result)

        if ops == "divide":
            r = num1 / num2
            result = f'The division of {num1} by {num2} is:  {r}'
        
        return jsonify(result)   ###output as json
        

if __name__=="__main__":
    app.run(host="0.0.0.0")
# render


## step by step guide to using the postman with this code

# 1. click addition button close to review (+)
# 2. select your method on the side, POST method for this!!!
# 3. use the url on postman https://red-musician-shilc.pwskills.app:5000/postman_action
# 4. Select "Body" then "raw" then "text:pick JSON"
# 5. Pass the data in as json in the column provided below for typing









