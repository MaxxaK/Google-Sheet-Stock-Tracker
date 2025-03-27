import gspread as goog
from oauth2client.service_account import ServiceAccountCredentials as SAC
from datetime import datetime

def connect(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = SAC.from_json_keyfile_name("credentials.json", scope)
    client = goog.authorize(credentials)
    return client.open(sheet_name).sheet1

def update(sheet, symbol, price):
    date = datetime.now().strftime("%m/%d/%Y")
    sheet.append_row([date, symbol, price])