import datetime
    
def logchange(action, details):
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"{ts} — {action}: {details}"
    with open("changes.log", "a") as f:
        f.write(line + "\n")

def show_history():
    try:
        with open("changes.log", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No history yet.")
