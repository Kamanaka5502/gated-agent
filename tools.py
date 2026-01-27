def run_tool(bucket: str, text: str) -> dict:
    if bucket == "billing":
        return {
            "previous_avg": "$82",
            "current_bill": "$146",
            "cause": "prorated charges due to address change mid-cycle",
            "fix_available": True
        }

    if bucket == "weather":
        return {
            "temp": "55F",
            "conditions": "Rainy"
        }

    return {"message": "No tool available"}
