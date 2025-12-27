class AlertRule:
    def __init__(self, symbol: str, condition: str, threshold: float):
        if condition not in ("above", "below"):
            raise ValueError("condition must be 'above' or 'below'")

        self.symbol = symbol
        self.condition = condition
        self.threshold = threshold

    def trigger(self, price: float) -> bool:
        if price is None:
            return False

        if self.condition == "above":
            return price > self.threshold

        return price < self.threshold
