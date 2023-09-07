from ebest_util import *

def cycle(username, iteration=50):
    init_util(username)

    start = get_account()
    price()
    for i in range(iteration):
        order(is_debug=True)
        time.sleep(0.3)
        order(is_buy=False, is_debug=True)
        time.sleep(0.3)

    end = get_account()
    print(f'실현손익: {format(end - start, ",")}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cycle("장준혁-모의투자", 1)

