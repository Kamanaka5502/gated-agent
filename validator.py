def validate_tool_result(result: dict, bucket: str) -> dict:
    required = {
        "billing": ["previous_avg", "current_bill", "cause"],
        "weather": ["temp", "conditions"]
    }

    keys = required.get(bucket, [])

    for key in keys:
        if key not in result:
            raise ValueError(f"Missing key '{key}' in tool result")

    return result
