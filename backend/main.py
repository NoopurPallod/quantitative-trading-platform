from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from portfolio_optimizer import optimize_portfolio
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)
from analyze import analyze_stock
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
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

    return analyze_stock(ticker)

class PortfolioRequest(BaseModel):
    stocks: list[str]

@app.post("/portfolio")
def portfolio(request: PortfolioRequest):

    return optimize_portfolio(
        request.stocks
    )