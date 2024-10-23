
class StockPortfolio:
    def __init__(self):
        # Initialize an empty portfolio as a dictionary with stock symbols and number of shares
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        """Add a stock to the portfolio."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, shares):
        """Remove a stock or a number of shares from the portfolio."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= shares:
                self.portfolio[symbol] -= shares
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
                print(f"Removed {shares} shares of {symbol} from your portfolio.")
            else:
                print(f"Error: You don't have enough shares to remove.")
        else:
            print(f"Error: {symbol} not found in your portfolio.")

    def fetch_stock_price(self, symbol):
        """Fetch real-time stock price using yfinance."""
        stock = yf.Ticker(symbol)
        try:
            # Get the most recent close price (real-time)
            price = stock.history(period="1d")['Close'][0]
            return price
        except:
            print(f"Error: Could not fetch data for {symbol}.")
            return None

    def view_portfolio(self):
        """Display the portfolio and calculate total value based on real-time prices."""
        print("\nYour Portfolio:")
        total_value = 0.0
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        for symbol, shares in self.portfolio.items():
            price = self.fetch_stock_price(symbol)
            if price:
                stock_value = shares * price
                total_value += stock_value
                print(f"{symbol}: {shares} shares @ ${price:.2f} each = ${stock_value:.2f}")
            else:
                print(f"{symbol}: {shares} shares (price unavailable)")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")


def main():
    portfolio = StockPortfolio()

    while True:
        print("Portfolio Management Options:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            symbol = input("Enter the stock symbol: ").upper()
            try:
                shares = int(input(f"How many shares of {symbol} do you want to add? "))
                if shares > 0:
                    portfolio.add_stock(symbol, shares)
                else:
                    print("Please enter a valid number of shares.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            symbol = input("Enter the stock symbol: ").upper()
            try:
                shares = int(input(f"How many shares of {symbol} do you want to remove? "))
                if shares > 0:
                    portfolio.remove_stock(symbol, shares)
                else:
                    print("Please enter a valid number of shares.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            portfolio.view_portfolio()

        elif choice == "4":
            print("Exiting the portfolio tracker.")
            break

        else:
            print("Invalid option. Please select a valid action.")


if __name__ == "__main__":
    main()
