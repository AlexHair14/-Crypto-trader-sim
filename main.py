from pycoingecko import CoinGeckoAPI
import time


def if_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True
    #if number is odd then function returns true


def if_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    # if number is even then function returns true


def if_list_full(list):
    if list:
        return True
    else:
        return False


def get_time():
    # gets the current time in Unix time
    Curr_time = str(time.time())
    Curr_time = (Curr_time[0:10])
    return Curr_time


def get_history_over_24(coin):
    while True:
        # 24 hour period
        Curr_time = get_time()
        Prev_Day = int(Curr_time) - 86400
        str(Prev_Day)
        TA = API.get_coin_market_chart_range_by_id(id=coin, vs_currency='usd', from_timestamp=Prev_Day, to_timestamp=Curr_time)
        TA = TA['prices']
        time.sleep(1.5)
        if if_list_full(TA):
            return TA


def get_price(coin):
    p = API.get_price(coin, 'usd')
    p = p[coin]
    p = p['usd']
    p = int(p)
    return p



'''
while program_on:
    TA = get_history_over_24('bitcoin')
    for item in TA:
        data_entry = item
        entry_time = data_entry[0]
        entry_price = data_entry[1]
        print(entry_time, entry_price) #This was for using the history but it doesn't give live feedback of price

'''

# creates an api object, so you can interact with the api
API = CoinGeckoAPI()

program_on = True
old_price = get_price('bitcoin')
wallet = 100
coin_asset = 0

while program_on:
    #so you don't spam requests
    time.sleep(5)
    # makes sure you are connected to server, probably not needed, but I thought it was cool
    server_responsive = API.ping()
    if server_responsive:

        # If New Price - Old price / old price * 100 = calc. This calculates the % increase or decrease
        current_price = get_price('bitcoin')
        percent_change = current_price - old_price
        percent_change = percent_change / old_price
        percent_change = percent_change * 100

        #if there is a percentage change from previous iteration then tell us
        if not percent_change == 0.0:
            print('percentage change:', percent_change)


        if percent_change > .015 and wallet > 0.01:
            # if asset is up by 15% or more we want to buy all we can with 90% of our wallet
            money_to_spend = wallet * 0.9
            new_asset = money_to_spend / current_price
            coin_asset =+ new_asset
            wallet =-money_to_spend
            print('wallet ammount:', wallet)
            print('coin asset amount:', coin_asset)


        if percent_change < -.015 and coin_asset > 0:
            # if asset is down by 15% or more we need to sell 100% of our crypto assets
            coin_to_sub = coin_asset
            coin_asset =- coin_to_sub
            cash_to_gain = coin_to_sub * current_price
            wallet =+ cash_to_gain
            print('wallet ammount:',wallet)
            print('coin asset amount:', coin_asset)

        # if we go into negative money it terminates the program
        if wallet < 0.01 and coin_asset == 0:
            program_on = False


        old_price = current_price
    else:
        print("No Server Response")









