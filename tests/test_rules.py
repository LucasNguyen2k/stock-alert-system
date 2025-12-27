import pytest
from src.rules import AlertRule

def test_above_rule_triggers():
    rule = AlertRule("AAPL", "above", 150)
    assert rule.trigger(160) is True
    assert rule.trigger(140) is False

def test_below_rule_triggers():
    rule = AlertRule("AAPL", "below", 100)
    assert rule.trigger(90) is True
    assert rule.trigger(110) is False

def test_invalid_condition():
    with pytest.raises(ValueError):
        AlertRule("AAPL", "equals", 100)

def test_none_price_does_not_trigger():
    rule = AlertRule("AAPL", "above", 150)
    assert rule.trigger(None) is False
