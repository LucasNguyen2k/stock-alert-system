from src.rules import AlertRule
from src.manager import AlertManager
from src.runner import AlertRunner
from src.console_notifier import ConsoleNotifier

def sample_price_provider():
    # Replace with a real price provider as needed
    return {"AAPL": 172, "MSFT": 245}

DEFAULT_RULES = [
    AlertRule("AAPL", "above", 170),
    AlertRule("MSFT", "below", 250),
]

def main():
    manager = AlertManager(DEFAULT_RULES)
    runner = AlertRunner(manager, sample_price_provider)
    alerts = runner.run_once()
    if alerts:
        ConsoleNotifier().send(alerts)

if __name__ == "__main__":
    main()