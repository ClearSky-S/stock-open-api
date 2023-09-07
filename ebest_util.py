import requests
import urllib3
import json

urllib3.disable_warnings()
BASE_URL = "https://openapi.ebestsec.co.kr:8080"
ACCESS_TOKEN = None

users = None


def printJSON(jsonData):
    print(json.dumps(jsonData, indent=2))


def init_util(username="장준혁-모의투자"):
    global ACCESS_TOKEN
    global users
    if users == None:
        with open('users.txt', 'rt', encoding='UTF8') as file:
            users = json.loads(file.read())
    print(f'로그인 시도: {username}')
    APP_KEY = users[username]["APP_KEY"]
    APP_SECRET = users[username]["APP_SECRET"]
    header = {"content-type": "application/x-www-form-urlencoded"}
    param = {"grant_type": "client_credentials", "appkey": APP_KEY, "appsecretkey": APP_SECRET, "scope": "oob"}
    PATH = "oauth2/token"
    URL = f"{BASE_URL}/{PATH}"
    request = requests.post(URL, verify=False, headers=header, params=param)
    ACCESS_TOKEN = request.json()["access_token"]
    if (ACCESS_TOKEN == None):
        print("로그인 실패")
        exit()
    print(request.json())
    print("로그인 완료")


def get_account():
    if (ACCESS_TOKEN == None):
        print("로그인 실패")
        exit()
    PATH = "stock/accno"
    URL = f"{BASE_URL}/{PATH}"
    header = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "tr_cd": "t0424",
        "tr_cont": "N",
        "tr_cont_key": "",
    }
    body = {
        "t0424InBlock":
            {
                "prcgb": "",
                "chegb": "",
                "dangb": "",
                "charge": "",
                "cts_expcode": ""
            }
    }
    request = requests.post(URL, headers=header, data=json.dumps(body))
    print(f"""계좌 잔고: {format(request.json()["t0424OutBlock"]["sunamt"], ',')}""")


def order(RecCnt=1):
    if (ACCESS_TOKEN == None):
        print("로그인 실패")
        exit()
    PATH = "stock/order"
    URL = f"{BASE_URL}/{PATH}"
    header = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "tr_cd": "CSPAT00601",
        "tr_cont": "N",
        "tr_cont_key": "",
    }
    body = {
        "CSPAT00601InBlock1": {
            "RecCnt": 1,
            "IsuNo": "A005930",
            "OrdQty": 2,
            "OrdPrc": 50000.0,
            "BnsTpCode": "2",
            "OrdprcPtnCode": "03",
            "PrgmOrdprcPtnCode": "00",
            "StslAbleYn": "0",
            "StslOrdprcTpCode": "0",
            "CommdaCode": "41",
            "MgntrnCode": "000",
            "LoanDt": "",
            "MbrNo": "000",
            "OrdCndiTpCode": "0",
            "StrtgCode": " ",
            "GrpId": " ",
            "OrdSeqNo": 0,
            "PtflNo": 0,
            "BskNo": 0,
            "TrchNo": 0,
            "ItemNo": 0,
            "OpDrtnNo": "0",
            "LpYn": "0",
            "CvrgTpCode": "0"
        }
    }
    request = requests.post(URL, headers=header, data=json.dumps(body))
    print(request.json())

    print(request.json()["rsp_msg"])



if __name__ == "__main__":
    init_util("장준혁-모의투자")
    get_account()
    order()
    get_account()
