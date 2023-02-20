import mysql.connector

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)

#CREATE WITHOUT CONDITION

def insert_into_table_without_condition(fields, values, tablename):
    my_database = db_connection.cursor()
    sql_statement = "INSERT INTO " + tablename + "(" + fields + ") VALUES(" + values + ")"
    print(sql_statement)
    try:
        my_database.execute(sql_statement)
        db_connection.commit()
        retval = "Success"
    except:
        retval = "Failed"
    db_connection.close()
    return retval

#GET ALL PRODUCTS DATA CONDITION

def get_products_list(table):
    my_database = db_connection.cursor(dictionary = True)
    sql_statement = "SELECT * FROM "+ table + ""
    try:
        my_database.execute(sql_statement)
        resp = my_database.fetchall()
    except:
        resp = {"Error":"No data recieved or error occured"}
    db_connection.close()    
    return resp

#GET PRODUCTS DATA WITH CONDITION    

def get_single_product(condition,table):
    my_database = db_connection.cursor(dictionary = True)
    sql_statement = "SELECT * FROM "+ table + " WHERE " + condition + ""
    try:
        my_database.execute(sql_statement)
        resp = my_database.fetchall()
    except:
        resp = {"Error":"No data recieved or error occured"}
    db_connection.close()    
    return resp   

#UPDATE PRODUCTS DATA WITH CONDITION    

def update_product(condition,updatestatement,table):
    my_database = db_connection.cursor()
    sql_statement = "UPDATE "  + table + " SET " + updatestatement + " WHERE " + condition + ""
    try:
        my_database.execute(sql_statement)
        db_connection.commit()
        retval = "Updated product successfully"
    except:
        retval = "Failed"
    db_connection.close()
    return retval

#DELETE PRODUCT DATA WITH CONDITION    

def delete_single_product(condition,table):
    my_database = db_connection.cursor()
    sql_statement = "DELETE "+ " FROM "  + table + " WHERE " + condition + ""
    print(sql_statement)
    try:
        my_database.execute(sql_statement)
        db_connection.commit()
        retval = "Removed product successfully"
    except:
        retval = "Failed"
    db_connection.close()
    return retval



