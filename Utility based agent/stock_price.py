import random
import time

class StockTradingAgent:
    def __init__(self):

        self.risk_tolerance = {"low": 0.5, "medium": 1.0, "high": 1.5}

    def decide_action(self, stock_price, trend, news, user_risk):
        # Calculate simple utility scores
        buy_score = (100 - stock_price) + (trend * 10) + (news * 5) * self.risk_tolerance[user_risk]
        sell_score = (stock_price - 100) - (trend * 5) - (news * 3) * self.risk_tolerance[user_risk]
        hold_score = 5


        if buy_score > sell_score and buy_score > hold_score:
            best_action = "Buy"
        elif sell_score > buy_score and sell_score > hold_score:
            best_action = "Sell"
        else:
            best_action = "Hold"

        return best_action, {"Buy": buy_score, "Sell": sell_score, "Hold": hold_score}


def generate_stock_data():
    time.sleep(2)
    stock_price = random.randint(80, 120)  # Random stock price
    trend = random.choice([-1, 0, 1])  # -1 = Down, 0 = Neutral, 1 = Up
    news = random.choice([-1, 0, 1])  # -1 = Negative, 0 = Neutral, 1 = Positive
    return stock_price, trend, news

def main():
    agent = StockTradingAgent()
    user_risk = random.choice(["low", "medium", "high"])  # Simulating user risk level

    while True:
        stock_price, trend, news = generate_stock_data()

        print("\nStock Market Data:")
        print("Stock Price:", stock_price)
        print("Trend:", "Up" if trend == 1 else "Down" if trend == -1 else "Stable")
        print("News Sentiment:", "Positive" if news == 1 else "Negative" if news == -1 else "Neutral")
        print("User Risk Tolerance:", user_risk.capitalize())


        best_action, scores = agent.decide_action(stock_price, trend, news, user_risk)

        print("\nUtility Scores:")
        for action, score in scores.items():
            print(f"{action}: {score:.2f}")

        print("\nRecommended Action:", best_action)
        print("----------------------------------")

if __name__ == "__main__":
    main()
