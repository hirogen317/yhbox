import logging
import psycopg2
import yaml

with open("config.yml", "r") as f:
    config = yaml.load(f.read())

def hello_http(request):

    connection = psycopg2.connect(host=config["host"], database=config["database"], user=config["user"],password=config["password"])

    print(connection.get_backend_pid())
    print(connection.get_backend_pid())
    cur = connection.cursor()
    print(cur)
    cur.execute("select version()")
    for row in cur:
        print(row)

    request_json = request.get_json()
    if request_json and 'name' in request_json:
        name = request_json['name']
    else:
        name = 'World'

    return 'Hello, {}!'.format(row)
