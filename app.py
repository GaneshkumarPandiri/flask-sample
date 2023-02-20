from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from operations.opeMethods import methods


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/checkapi")
@cross_origin()
def get_sample_response():
    return {
        "Name" : "GaneshKumar Pandiri",
        "age" : "26"
    }

#==========PRODUCTS======START==============#

@app.route("/products", methods  = ["POST", "GET"])
@cross_origin()
def products_response():
    if request.method == "POST":
        req = request.json
        resp = methods.insert_products(req)
        return resp
    if request.method == "GET":
        resp = methods.get_products()
        return jsonify(resp)   

@app.route("/product/<int:id>", methods  = ["PUT", "GET" , "DELETE"])
@cross_origin()
def product_response(id):
    if request.method == "PUT":
        req = request.json
        resp = methods.modify_product(id,req)
        return resp
    if request.method == "GET":
        resp = methods.get_product(id)
        return jsonify(resp)
    if request.method == "DELETE":
        resp = methods.remove_product(id)  
        return jsonify(resp)  

#==========PRODUCTS======END==============#  


#==========REVIEWS======START==============# 

@app.route("/product/reviews", methods  = ["POST", "GET"])
@cross_origin()
def reviews_response():
    if request.method == "POST":
        req = request.json
        resp = methods.insert_reviews(req)
        return resp
    if request.method == "GET":
        resp = methods.get_reviews()
        return jsonify(resp) 




#==========REVIEWS======END==============# 



    


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")