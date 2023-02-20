from operations.dbOperations import dbQueries
from operations.common import const
def get_products():
    resp = dbQueries.get_products_list("`products`")
    respsucc = {"responsefor":"productlist","responseto":"UI","responsedata": resp }
    return respsucc

def insert_products(reqData):
    if isinstance(reqData, dict):
        fields = const.products_const
        data = '","'.join(reqData['requestdata'].values())
        data = '"' + data + '"'
        resp = dbQueries.insert_into_table_without_condition(fields,data,"products")
        if resp == "Success":
            respsucc = {}
            respsucc = {"responseid": reqData['requestid'], "responsefor":"createproduct","responseto":"UI","responsedata": "Product Created Successfully" }
            return respsucc
        else:
            respfail = {}
            respfail = {"responseid": reqData['requestid'], "responsefor":"createproduct","responseto":"UI","responsedata": "Product Creation Failed"}
            return  respfail

def modify_product(id,req):
    condition = "`id` =" + str(id) 
    data = req["requestdata"]
    prodname = data["productName"]
    desp = data["description"]
    brand = data["brand"]
    price = data["price"]
    ratings = data["ratings"]
    imgURL = data["imageURL"]
    statement = "`productName`='" + prodname + "'" + "," + "`description`='" + desp + "'" + "," + "`brand`='" + brand + "'"+ "," + "`price`='" + price + "'" + ","+ "`ratings`='" + ratings + "'" + ","+ "`imageURL`='" + imgURL + "'"
    resp = dbQueries.update_product(condition, statement,"`products`")
    resp = {"responsefor":"productlist","responseto":"UI","responsedata": resp }
    return resp

def get_product(id):
    condition = "`id` =" + str(id) 
    resp = dbQueries.get_single_product(condition,"`products`")
    respsucc = {"responsefor":"productlist","responseto":"UI","responsedata": resp }
    return respsucc

def remove_product(id):
    condition = "`id` =" + str(id) 
    resp = dbQueries.delete_single_product(condition,"`products`")
    respsucc = {"responsefor":"productlist","responseto":"UI","responsedata": resp }
    return respsucc

#===============================

def insert_reviews(req):
    pass

def get_reviews():
    pass

