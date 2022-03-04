from pycoingecko import CoinGeckoAPI
import time

API = CoinGeckoAPI()

assets = {}

wallet = 100


def get_time():
    # gets the current time in Unix time
    curr_time = str(time.time())
    curr_time = (curr_time[0:10])
    return curr_time


def get_price(coin):
        API = CoinGeckoAPI()
        p = API.get_price(coin,'usd')
        p = p[coin]
        p = p['usd']
        p = int(p)
        return p


old_price = get_price('bitcoin')

def calc_percent_change(old_price):
    # If New Price - Old price / old price * 100 = calc. This calculates the % increase or decrease
    current_price = get_price('bitcoin')
    percent_change = current_price - old_price
    percent_change = percent_change / old_price
    percent_change = percent_change * 100
    return percent_change


def buy_asset(asset_name, percent_to_buy, wallet, asset_dic):
    if wallet < 0.01:
        return False
    money_to_spend = wallet * percent_to_buy
    current_price = get_price(asset_name)
    new_asset = money_to_spend / current_price
    wallet -= money_to_spend

    # if there are assets
    if asset_dic:
        # if the asset we are buying is in the dictionary
        if asset_dic.get(asset_name):
            # updates asset dictionary to reflect new amount of asset owned
            amount_prev_owned = asset_dic.get(asset_name)
            total_of_asset = amount_prev_owned + new_asset
            asset_dic[asset_name] = total_of_asset


    #if there are no assets
    if not asset_dic:
        # create a new asset
        asset_dic.update({asset_name : (new_asset)})
        print('there are no assets')
    print(asset_dic)
    print('wallet amount:', wallet)
    return


def sell_asset(asset_name, percent_to_sell, wallet, asset_dic):
    current_price = get_price(asset_name)
    # if asset_dictionary has stuff in it
    if asset_dic:
        #if asset we are trying to sell is in the asset dictionary
        if asset_dic.get(asset_name):
            # find how much I own
            amount_prev_owned = asset_dic.get(asset_name)

            amount_selling = amount_prev_owned * percent_to_sell
            # subtract amount selling from amount owned
            total_of_asset = amount_prev_owned - amount_selling
            # update the new total asset amount after selling
            asset_dic[asset_name] = total_of_asset


    # if there is nothing to sell then returns as false
    else:
        return False
    # need to get amount to subtract from

    cash_to_gain = amount_selling * current_price
    wallet += cash_to_gain
    print(asset_dic)
    print('wallet amount:',wallet)


program_on = True

connection_attemps = 0

asset_to_trade = input('what coin do you want to trade')

while program_on:
    time.sleep(5)

    percent_change = calc_percent_change(old_price)
    if not percent_change == 0:
        print(percent_change)
    if percent_change > .015:
        # if asset is up by .015% or more we want to buy all we can with 90% of our wallet
        buy_asset('bitcoin', 0.9, wallet,assets)

    if percent_change < 0.015:
        # if asset is down by .015% or more we need to sell 100% of our crypto assets
        sell_asset('bitcoin', 0.9, wallet, assets)

    current_price = get_price('bitcoin')
    old_price = current_price


