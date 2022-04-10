import yfinance as yf


# need to create a program which finds the best asset to trade 
asset_to_trade = 'bitcoin'

# These could be used to adjust how much money you spend on an asset or sell 
# based on how confident you are on what the market is doing 
purchase_percentage = 0.9
selling_percentage = 0.9

total_cash = 100 

# When a transaction occurs how much is the asset worth
price_of_asset = 1

# How much of an asset do you own before anything happens 
amount_of_asset_before_sale = 100 

class info:
    def __init__(self):
        self.cash = total_cash
        self.name = asset_to_trade
        self.percent_to_buy = purchase_percentage
        self.percent_to_sell = selling_percentage
        self.current_price = price_of_asset
        self.asset_before_sale = amount_of_asset_before_sale


    def buy_asset(self):
        money_to_spend = self.cash * self.percent_to_buy
        new_asset_amount = money_to_spend / self.current_price
        cash_after = self.cash - money_to_spend
        buying_info = {
            'Total cash after trans' : cash_after,
            'Total of new asset' : new_asset_amount,
            'Money spent' : money_to_spend,
        }
        return buying_info
        

    def sell_asset(self):
        amount_selling = self.asset_before_sale * self.percent_to_sell
        cash_after = amount_selling * self.current_price
        new_asset_amount = self.asset_before_sale - amount_selling
        selling_info = {
            'Total cash after trans' : cash_after,
            'Total of new asset' : new_asset_amount,
            'Amount of asset sold' : amount_selling,
        }
        return selling_info

