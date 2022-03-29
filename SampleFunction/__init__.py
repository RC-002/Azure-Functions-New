import logging
import os
from pickle import TRUE
import mysql.connector
import struct
import azure.functions as func
import urllib.request
import json
import os
import ssl

currentRowId = 0

def main(req: func.HttpRequest) -> func.HttpResponse:
 
    data1 = req.params.get('data')
    logging.info('request Data: ' + data1)
    newData = str(data1)
    logging.info('newData: ' + newData)
    logging.info('Python HTTP trigger function processed a request.')
    logging.info('dbId: ' + '-1')
    dbId = updateStatus(-1, 'Python HTTP trigger function processed a request.')
    logging.info('dbId: ' + str(dbId))
    name = req.params.get('name')
    logging.info('name: ' + name)
    code = req.params.get('code')
    logging.info('code: ' + code)
    data = json.loads(data1)
    logging.info('data value set')
    inputData = json.dumps(data)
    retData = allowSelfSignedHttps(True, data, dbId)

    if not name:
        try:
            req_body = req.get_json()    
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if name:      
        return func.HttpResponse(retData)
    else:
        return func.HttpResponse(
             retData,
             status_code=200
        )


def updateStatus(currentRowId , status):
    cnx = mysql.connector.connect(user='rohanadmin@rohanvit', password='RohanUsesGithub123',
                                host='rohanvit.mysql.database.azure.com',
                                database='creditcard_fraud_check')
    logging.info('Successfully connected to the Database.')
    logging.info('currentRowId: ' + str(currentRowId))
    logging.info('status: ' + status)

    cursor = cnx.cursor()
    if (currentRowId ==-1):
        currentRowId = cursor.lastrowid
        cursor.execute("INSERT INTO service_invoke_details (id, status) VALUES (%s,  %s);", ( currentRowId,status))
    else:
        cursor.execute("INSERT INTO service_invoke_details (id, status) VALUES (%s,  %s);", ( currentRowId,status))        
    logging.info("Finished Inserting into table.")
    cnx.commit()
    cursor.close()
    cnx.close()
    return currentRowId

def allowSelfSignedHttps(allowed, data, dbId):
    logging.info("In the Function allowSelfSignedHttps")
    updateStatus(dbId, 'In the Function allowSelfSignedHttps')

    url = 'http://9fa411ac-eda5-4264-8463-a198619111da.westus.azurecontainer.io/score'
    api_key = '02vTdOYQDgPjLXqZ2cSx7XrypRcFIprT' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    body = str.encode(json.dumps(data))
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        logging.info(result)
        updateStatus(dbId, 'Successfully Processed')
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        updateStatus(dbId, error.info())
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))


    

   