import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 175
}
portfolio = []
total_portfolio_value = 0
print("______ Stock Portfolio Tracker _______")
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").strip().upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter the quantity for {stock}:"))
        price = stock_prices[stock]
        total = price * quantity
        total_portfolio_value += total

        portfolio.append([stock, quantity, price, total])
        print(f"Added {stock}: Quantity: {quantity}, Price : ${price}, Total Investment : ${total}")
    else:
        available_stocks = ", ".join(stock_prices.keys())
        print(f"Stock not found! Please try: {available_stocks}")
print("\n" + "="*35)
print(f"Total Portfolio Value: ${total_portfolio_value}")
print("="*35)
if portfolio:     
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Investment"])
        writer.writerows(portfolio)
    print("Portfolio saved successfully to portfolio.csv!")

