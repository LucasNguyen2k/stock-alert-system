from src.manager import AlertManager

class AlertRunner:
    def __init__(self, manager: AlertManager, price_provider):
        """
        price_provider: callable that returns price dict
        """
        self.manager = manager
        self.price_provider = price_provider

    def run_once(self):
        print("I am runner")
        prices = self.price_provider()
        return self.manager.evaluate(prices)
