def route_bucket(text: str) -> str:
    text = text.lower()

    if "bill" in text or "moved" in text:
        return "billing"

    if "weather" in text or "rain" in text:
        return "weather"

    return "unknown"
