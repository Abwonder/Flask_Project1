from flask import Flask, request, render_template, jsonify   ### all library are needed for this job!!!

app = Flask(__name__)

### home page declaration
@app.route("/")  ## declared to map the function to url
def home_pager():
    return render_template("index.html")  ## index in same directory although subfolderl. ## front end are to provide this!!! both bonus if you are good with html

## Dealing with the math("/")

@app.route("/math", methods= ["POST"]) ## where bond everything to route on url; Also specify how to make the data available!! method == POST
def math_op():
    if(request.method == "POST"):  ## mean it will not be visible on the url, gotten thru form
       ## all the client side data entry will need to be obtainedbo, both POST and GET can be use to get data
       ## differences is that POST will not be visible on the url, while GET will be!!
        ops = request.form["operation"]  ## operatin is label -- check this on the source page on the url or check the source code index.html
        num1 = request.form["num1"]  ## this is the second input label on the page
        num2 = request.form["num2"]  ## same use the index.html to get this information
        if ops == "add":
            r = int(num1) + int(num2)
            result = f'The sum of {num1} and {num2} is:  {r}'
            # return render_template("results.html", result = result)

        if ops == "subtract":
            r = int(num1) - int(num2)
            result = f'The subtraction of {num2} from {num1} is:  {r}'
            # return render_template("results.html", result = result)

        if ops == "<multiply":
            r = int(num1) * int(num2)
            result = f'The multiplication of {num1} and {num2} is:  {r}'
            # return render_template("results.html", result = result)

        if ops == "divide":
            r = int(num1) / int(num2)
            result = f'The division of {num1} by {num2} is:  {r}'
        
        return render_template("results.html", result = result)
        

if __name__=="__main__":
    app.run(host="0.0.0.0")
# render
