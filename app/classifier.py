CATEGORY_KEYWORDS = {
    "billing": ["refund", "charge", "invoice", "payment", "billing", "subscription"],
    "access": ["login", "log in", "password", "locked out", "sign in"],
    "bug": ["error", "crash", "bug", "not working", "broken", "fails"],
}

URGENT_KEYWORDS = ["urgent", "asap", "immediately", "outage", "system down"]


def classify_ticket(text: str) -> dict:
    lowered = text.lower()

    category = "general"
    for name, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            category = name
            break

    priority = "high" if any(word in lowered for word in URGENT_KEYWORDS) else "normal"

    return {"category": category, "priority": priority}