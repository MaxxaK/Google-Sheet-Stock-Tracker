from get_stocks import get_stock_price
from google_sheets import connect, update
import schedule
import time

def check_and_update(sheet, symbol):
    price = round(get_stock_price(symbol),2)
    if price is not None:
        formatted_price = f"${price:.2f}"
        update(sheet, symbol, formatted_price)
        print(f"Updated {symbol} with price {price}")
    else:
        print(f"Failed to fetch data for {symbol}")

def daily_task(sheet, symbols):
    for symbol in symbols:
        check_and_update(sheet, symbol)
    sheet.append_row([])

if __name__ == "__main__":
    symbols = input("What stocks would you like? Separate By Commas.") 
    symbols = [symbol.strip().upper() for symbol in symbols.split(",")]
    sheet = connect("Stock Tracker Bot")

    schedule.every().day.at("10:46").do(daily_task, sheet=sheet, symbols=symbols)

    print("Scheduler running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
