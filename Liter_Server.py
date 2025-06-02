import mariadb
import time
import json

DB_USER = "admin"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = 3306
DATA_JSON_PATH = "data.json"

def hent_liter_drukket():
    try:
        conn = mariadb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database="ølbord"
        )
        cur = conn.cursor()
        cur.execute("SELECT liter_drukket FROM drikke_logg WHERE id = 1")
        result = cur.fetchone()
        conn.close()
        return float(result[0]) if result else 0.0
    except:
        return 0.0

def hent_pris_carlsberg():
    try:
        conn = mariadb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database="øl"
        )
        cur = conn.cursor()
        cur.execute("SELECT price FROM øl WHERE id = 5")
        result = cur.fetchone()
        conn.close()
        return float(result[0]) if result else 0.0
    except:
        return 0.0

if name == "main":
   try:
        while True:
            liter = hent_liter_drukket()
            pris = hent_pris_carlsberg()
            data = {
                "liter": round(liter, 2),
                "total_price": round(liter * pris, 2)
            }
            with open(DATA_JSON_PATH, "w") as f:
                json.dump(data, f)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopper...")
