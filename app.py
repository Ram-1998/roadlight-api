import flask
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import json
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Api DATA").sheet1

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    list_of_hashes = sheet.get_all_records()
    return json.dumps(list_of_hashes)


@app.route('/on', methods=['GET'])
def on():
    now = datetime.datetime.now()
    row = ["On",now.strftime("%Y-%m-%d"),now.strftime("%H:%M:%S")]
    index = 2
    sheet.insert_row(row, index)
    return "<h1>On page</h1>"

@app.route('/off', methods=['GET'])
def off():
    now = datetime.datetime.now()
    row = ["Off",now.strftime("%Y-%m-%d"),now.strftime("%H:%M:%S")]
    index = 2
    sheet.insert_row(row, index)
    return "<h1>Off page</h1>"

app.run()
