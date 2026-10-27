from app.classifier import classify_ticket


def test_billing_ticket():
    result = classify_ticket("I was charged twice for my subscription")
    assert result["category"] == "billing"


def test_access_ticket():
    result = classify_ticket("I can't log in to my account")
    assert result["category"] == "access"


def test_bug_ticket():
    result = classify_ticket("The app crashes when I open settings")
    assert result["category"] == "bug"


def test_unmatched_ticket_is_general():
    result = classify_ticket("Do you have an office in Belfast?")
    assert result["category"] == "general"


def test_urgent_ticket_is_high_priority():
    result = classify_ticket("Our system down since this morning, please fix asap")
    assert result["priority"] == "high"


def test_normal_priority_by_default():
    result = classify_ticket("Question about my account")
    assert result["priority"] == "normal"


def test_matching_ignores_case():
    result = classify_ticket("REFUND please")
    assert result["category"] == "billing"