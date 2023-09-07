import requests
import urllib3
import json
urllib3.disable_warnings()

def printJSON(jsonData):
    print(json.dumps(jsonData, indent=2))


APP_KEY = "PSqzdFXd4TS8ALTXVFDt1LDJaBcmtZEU3I3q"
APP_SECRET = "DJtieJ4ii5Wsq2mpfFz9OpLnmj86mczW"
header = {"content-type": "application/x-www-form-urlencoded"}
param = {"grant_type": "client_credentials", "appkey": APP_KEY, "appsecretkey": APP_SECRET, "scope": "oob"}
PATH = "oauth2/token"
BASE_URL = "https://openapi.ebestsec.co.kr:8080"
URL = f"{BASE_URL}/{PATH}"
request = requests.post(URL, verify=False, headers=header, params=param)
ACCESS_TOKEN = request.json()["access_token"]
print(json.dumps(request.json(),indent=2))
# print(ACCESS_TOKEN)
header = {
    "content-type":"application/json; charset=utf-8",
    "authorization": f"Bearer {ACCESS_TOKEN}",
    "tr_cd":"t0424",
    "tr_cont":"N",
    "tr_cont_key":"",
}
body = {
  "t0424InBlock": {
    "prcgb": "",
    "chegb": "",
    "dangb": "",
    "charge": "",
    "cts_expcode": ""
  }
}

PATH = "stock/accno"
BASE_URL = "https://openapi.ebestsec.co.kr:8080"
URL = f"{BASE_URL}/{PATH}"
request = requests.post(URL, headers=header, data=json.dumps(body))
printJSON(request.json())