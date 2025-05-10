
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../database/ink_stock.db')


def connect():
    return sqlite3.connect(DB_PATH)

def list_colors_by_model(id_models):
    con = connect()
    cur = con.cursor()
    cur.execute("""
        SELECT c.id, c.name, s.amount
        FROM colors c
        LEFT JOIN stock s ON s.id_colors = c.id
        WHERE c.id_models = ? 
    """, (id_models,))
    data = cur.fetchall()
    con.close()
    return data

def update_quantity(new_amount, id_colors):
    con = connect()
    cur = con.cursor()
    cur.execute("UPDATE stock SET amount = ? WHERE id_colors = ?", (new_amount, id_colors))
    con.commit()
    con.close()
    
    