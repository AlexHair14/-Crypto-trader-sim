def if_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True
    # if number is odd then function returns true


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


def get_history_over_24(coin):
    while True:
        # 24 hour period
        curr_time = get_time()
        prev_Day = int(curr_time) - 86400
        str(prev_Day)
        TA = API.get_coin_market_chart_range_by_id(id=coin, vs_currency='usd', from_timestamp=prev_Day, to_timestamp=curr_time)
        TA = TA['prices']
        time.sleep(1.5)
        if if_list_full(TA):
            return TA

'''
while program_on:
    TA = get_history_over_24('bitcoin')
    for item in TA:
        data_entry = item
        entry_time = data_entry[0]
        entry_price = data_entry[1]
        print(entry_time, entry_price) #This was for using the history but it doesn't give live feedback of price

'''

# makes sure you are connected to server, probably not needed, but I thought it was cool
server_responsive = API.ping()

if server_responsive:

else:
    print("No Server Response")
    connection_attemps += 1
    time.sleep(60)
    if connection_attemps == 10:
        program_on = False
