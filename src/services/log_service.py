import os
import json
from datetime import datetime
from .log_model import StockLog

LOG_FILE = os.path.join(os.path.dirname(__file__), '../../logs/stock_log.json')

def save_log_entry(log: StockLog):
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        logs = load_logs()
        logs.append(log.__dict__)
        with open(LOG_FILE, 'w') as f:
            json.dump(logs, f, indent=4, default=str)
    except Exception as e:
        print("Erro ao salvar log: ", e)

def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        return json.load(f)