from src.rules import AlertRule
from src.manager import AlertManager

def test_multiple_rules_trigger():
    rules = [
        AlertRule("AAPL", "above", 150),
        AlertRule("MSFT", "below", 250)
    ]

    manager = AlertManager(rules)

    prices = {
        "AAPL": 160,
        "MSFT": 300
    }

    alerts = manager.evaluate(prices)

    assert len(alerts) == 1
    assert alerts[0]["symbol"] == "AAPL"

def test_missing_symbol_is_ignored():
    rules = [AlertRule("GOOG", "above", 100)]
    manager = AlertManager(rules)

    alerts = manager.evaluate({"AAPL": 150})
    assert alerts == []
