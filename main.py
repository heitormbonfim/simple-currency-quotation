# # import app, and builder that connects the GUI
# # create application
# # create build function

# Default initialization
from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file('screen.kv') # this is the ROOT file being loaded

class MyApplication(App):
    def build(self):
        return GUI
# Default initialization
    def on_start(self): # self means get "MyApplication class" 
        dollar_bid = self.get_bid('USD')
        pound_bid = self.get_bid('EUR')
        bitcoin_bid = self.get_bid('BTC')
        ethereum_bid = self.get_bid('ETH')
        
        # getting the ids from 'screen.kv'
        self.root.ids['dollar'].text = f'1 Dollar = R${dollar_bid}'
        self.root.ids['pound'].text = f'1 Pound = R${pound_bid}'
        self.root.ids['bitcoin'].text = f'1 Bitcoin = R${bitcoin_bid}'
        self.root.ids['ethereum'].text = f'1 Ethereum = R${ethereum_bid}'

    # function to get bid from api 
    def get_bid(self, currency):
        link = f'https://economia.awesomeapi.com.br/last/{currency}-BRL'
        request = requests.get(link)
        request_data = request.json()
        bid = request_data[f'{currency}BRL']['bid'] # getting bid from json
        return bid

 

# To run the application
MyApplication().run()
