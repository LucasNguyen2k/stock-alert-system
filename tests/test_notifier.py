from src.console_notifier import ConsoleNotifier

def test_console_notifier_does_not_crash(capsys):
    notifier = ConsoleNotifier()

    alerts = [{
        "symbol": "AAPL",
        "condition": "above",
        "threshold": 150,
        "price": 170
    }]

    notifier.send(alerts)

    captured = capsys.readouterr()
    assert "AAPL" in captured.out

