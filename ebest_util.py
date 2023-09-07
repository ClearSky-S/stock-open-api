import requests
import urllib3
import json
import time

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
    print(f'-------- 로그인 시도: {username} --------')
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
    print("---잔고---")
    print(request.json())
    print(f"""계좌 잔고: {format(request.json()["t0424OutBlock"]["sunamt"], ',')}""")
    return request.json()["t0424OutBlock"]["sunamt"]


def order(is_buy=True):
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
            "IsuNo": "A459580",
            "OrdQty": 1,
            # "OrdPrc": 1010470.0,
            "BnsTpCode": "2" if is_buy else "1",
            "OrdprcPtnCode": "03",
            "MgntrnCode": "000",
            "LoanDt": "",
            "OrdCndiTpCode": "0"
        }
    }
    request = requests.post(URL, headers=header, data=json.dumps(body))
    print(request.json())

    print(request.json()["rsp_msg"])


def price():
    if (ACCESS_TOKEN == None):
        print("로그인 실패")
        exit()
    PATH = "stock/market-data"
    URL = f"{BASE_URL}/{PATH}"
    header = {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "tr_cd": "t1102",
        "tr_cont": "N",
        "tr_cont_key": "",
    }
    body = {
        "t1102InBlock": {
            "shcode": "459580"
        }
    }
    request = requests.post(URL, headers=header, data=json.dumps(body))
    print(request.json())

    print(request.json()["rsp_msg"])


if __name__ == "__main__":
    init_util("장준혁-모의투자")

    start = get_account()
    price()
    for i in range(20):
        order()
        time.sleep(0.5)
        order(is_buy=False)
    end = get_account()
    print(f'차액: {format(end - start, ",")}')
