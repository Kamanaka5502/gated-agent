from fastapi import FastAPI, Request
from gate import route_bucket
from tools import run_tool
from validator import validate_tool_result

app = FastAPI()

@app.post("/handle")
async def handle(req: Request):
    data = await req.json()
    user_input = data["input"]

    bucket = route_bucket(user_input)
    tool_result = run_tool(bucket, user_input)
    validated = validate_tool_result(tool_result, bucket)

    return {
        "bucket": bucket,
        "result": validated
    }
