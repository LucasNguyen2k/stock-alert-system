from src.rules import AlertRule
from src.manager import AlertManager
from src.runner import AlertRunner

def fake_price_provider():
    return {
        "AAPL": 170,
        "MSFT": 200
    }

def test_runner_triggers_alerts():
    rules = [
        AlertRule("AAPL", "above", 150),
        AlertRule("MSFT", "below", 250)
    ]

    manager = AlertManager(rules)
    runner = AlertRunner(manager, fake_price_provider)

    alerts = runner.run_once()

    assert len(alerts) == 2
