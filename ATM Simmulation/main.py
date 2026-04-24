import data

FILE_NAME = "atm_data.txt"

def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            lines = f.readlines()
            data.balance = float(lines[0].strip())
            data.transactions = [line.strip() for line in lines[1:]]
    except:
        data.balance = 0
        data.transactions = []

def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write(str(data.balance) + "\n")
        for t in data.transactions:
            f.write(t + "\n")