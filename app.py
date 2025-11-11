from flask import Flask
import os
import csv

app = Flask(__name__)

@app.route("/")
def index():
    equity_path = "logs/daily_equity.csv"
    trades_path = "logs/trades.csv"
    
    equity_data = []
    trades_data = []
    
    if os.path.exists(equity_path):
        with open(equity_path, 'r') as f:
            reader = csv.DictReader(f)
            equity_data = list(reader)
    
    if os.path.exists(trades_path):
        with open(trades_path, 'r') as f:
            reader = csv.DictReader(f)
            trades_data = list(reader)
    
    latest_equity = equity_data[-1]["equity"] if equity_data else "0"
    last_trade = trades_data[-1] if trades_data else None
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Trading Dashboard</title>
    <style>
        body {{ font-family: Arial; padding: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; }}
        h1 {{ color: #333; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }}
        .metric {{ background: #e
