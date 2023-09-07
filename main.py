from ebest_util import *

def cycle(username, iteration=50):
    init_util(username)

    start = get_account()
    price()
    for i in range(iteration):
        order()
        time.sleep(0.3)
        order(is_buy=False)
        time.sleep(0.3)

    end = get_account()
    print(f'차액: {format(end - start, ",")}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cycle("장준혁", 50)

