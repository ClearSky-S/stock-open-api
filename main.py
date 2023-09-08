import os, sys, pickle
import argparse, sys

import datetime
from ebest_util import *


def cycle(username, iteration=50, is_debug=False):
    init_util(username)

    start = get_account()
    if(is_debug):
        price()
    print(f"거래 중입니다. 기다려 주세요. 예상 소요 시간 : {0.6*iteration}초")
    print(f"예상 종료 시간: {datetime.datetime.now() + datetime.timedelta(seconds=0.6*iteration)}")
    for i in range(iteration):
        order(is_debug=is_debug)
        time.sleep(0.3)
        order(is_buy=False, is_debug=is_debug)
        time.sleep(0.3)

    end = get_account()
    print(f'실현손익: {format(end - start, ",")}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 실행 인자에 이름을 넣어 줘야 함
    for i in range(10):
        print(f"-------------------{i}-------------------")
        cycle(sys.argv[1], 50)
        print()
        print()
    print("-------------------종료-------------------")

# 실행
# python main.py 장준혁-모의투자

"""
python main.py 장준혁
python main.py 장재혁
python main.py 장진영
python main.py 박윤조
python main.py 심중섭
python main.py 오정임
python main.py 이석현

"""