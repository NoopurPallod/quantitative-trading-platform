import os
import sys

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from portfolio_optimizer import optimize_portfolio
from analyze import analyze_stock
from validation import validate_stock_list

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():

    return {
        "message": "Trading Platform API Running"
    }

@app.get("/analyze")
def analyze(ticker: str):

    if not ticker.strip():
        raise HTTPException(
            status_code=400,
            detail="Ticker cannot be empty"
        )

    try:
        return analyze_stock(ticker)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        ) from exc

class PortfolioRequest(BaseModel):
    stocks: list[str]

@app.post("/portfolio")
def portfolio(request: PortfolioRequest):
    try:
        stocks = validate_stock_list(request.stocks)
        return optimize_portfolio(stocks)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
