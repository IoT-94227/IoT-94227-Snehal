from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/soil_moisture')
def create_soil_moistures():
    
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')
    reading_time = request.form.get('reading_time')
  

    query = f"insert into soil_moisture values({sensor_id}, {moisture_level}, '{reading_time}');"

    #print(query)
    
    executeQuery(query=query)

    return "soil_moistures is added successfully"

@server.get('/soil_moisture')
def retrieve_soil_moistures():
    
    query = "select * from soil_moisture;"

    data = executeSelectQuery(query=query)

    return f"soil_moistures : {data}"

@server.put('/soil_moisture')
def update_soil_moistures():

    sensor_id= request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')

    query = f"update soil_moisture SET moisture_level = '{moisture_level}' where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "sensor_id is updated successfully"

@server.delete('/soil_moisture')
def delete_soil_moistures():
    
    sensor_id = request.form.get('sensor_id')

    query = f"delete from soil_moisture where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "soil_moisture is deleted successfully"

if __name__ == "__main__":
    # Disable debug mode in production environments
    server.run(host="0.0.0.0", port=4000, debug=False)