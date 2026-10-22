from fastapi import FastAPI

app = FastAPI()

FLIGHTS = {"AI101": "On time", "6E202": "Delayed"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/flights/{code}")
def flight_status(code: str):
    return {"flight": code.upper(), "status": FLIGHTS.get(code.upper(), "Unknown")}
