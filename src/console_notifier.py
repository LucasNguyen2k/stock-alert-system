from src.notifier import Notifier

class ConsoleNotifier(Notifier):
    def send(self, alerts: list[dict]):
        for alert in alerts:
            
            print(
                f"[ALERT] {alert['symbol']} "
                f"{alert['condition']} {alert['threshold']} "
                f"(price={alert['price']})"
            )
