from src.rules import AlertRule

class AlertManager:
    def __init__(self, rules: list[AlertRule]):
        self.rules = rules

    def evaluate(self, prices: dict) -> list[dict]:
        """
        prices example:
        {
            "AAPL": 155.0,
            "MSFT": 300.0
        }
        """
        triggered = []

        for rule in self.rules:
            price = prices.get(rule.symbol)
            if rule.trigger(price):
                triggered.append({
                    "symbol": rule.symbol,
                    "condition": rule.condition,
                    "threshold": rule.threshold,
                    "price": price
                })

        return triggered
