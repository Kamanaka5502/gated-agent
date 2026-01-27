# gated-agent

LLMs as deterministic infrastructure: a gated request pipeline that makes AI reliable in production.

---

Most LLM failures are not model failures.  
They are routing, state, and concurrency failures.

This repo shows a ~200 line request pipeline that turns an LLM from a “chatbot” into reliable infrastructure.

---

## Core Idea

**Gate user input → route by bucket → tools provide truth → LLM formats only**

The model never decides what to do.  
It only decides how to say it.

User → Gate → Bucket → Entity Extract → Tool → Validator → LLM → Logs → Learn


---

## Why this exists

Typical agent architecture:

- LLM decides which tools to call
- Hallucinated actions
- Lost conversational state
- Concurrency and retry issues

This pipeline:

- Deterministic routing
- Tool-driven truth
- Session locks
- Schema validation
- Logs that improve the gate over time

---

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload

curl -X POST http://localhost:8000/handle \
  -H "Content-Type: application/json" \
  -d '{"input":"I moved last week and my bill is high","session":{"user_id":"123"}}'

Philosophy

Rules decide when
Tools decide what
LLM decides how

Boring. Deterministic. Production-safe.
