# @LearnUpwards
# Get real-time stock price
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_latest_price(ticker):
    host = "https://www.google.com"
    api = f"finance/quote/{ticker}:NASDAQ"
    url = f"{host}/{api}"
    html = requests.get(url)
    # Parse the HTML
    soup = BeautifulSoup(html.text,
                         'html.parser')
    text_val = soup.find('div', attrs={
        'class': 'YMlKec fxKbKc'
    }).text
    return text_val
if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    price = get_latest_price(ticker)
    date = datetime.now().date()
    print(f'{ticker} price on {date} : {price}')
