from flask import Flask, request, jsonify
import tkinter as tk
import threading
import queue

# Flask 서버 초기화
app = Flask(__name__)
request_queue = queue.Queue()

def tkinter_mainloop():
    root = tk.Tk()
    root.withdraw()

    def check_queue():
        try:
            table, items, call_staff = request_queue.get_nowait()

            popup = tk.Toplevel()
            popup.title("[Serving Request]")
            popup.geometry("500x500")

            tk.Label(popup, text=f"[Request Table {table}]", font=("Arial", 16)).pack(pady=10)
            for item, count in items.items():
                if count > 0:
                    tk.Label(popup, text=f"{item.capitalize()}: {count}", font=("Arial", 15)).pack()
            if call_staff:
                tk.Label(popup, text="Employee Call !", font=("Arial", 14), fg="red").pack(pady=10)

#            def on_confirm():
#                print(f"[INFO] 로봇 출동 - Table {table}, Items: {items}, Staff Call: {call_staff}")
#                popup.destroy()

#            tk.Button(popup, text="로봇 출동하기", command=on_confirm, font=("Arial", 12)).pack(pady=20)

        except queue.Empty:
            pass
        root.after(500, check_queue)

    check_queue()
    root.mainloop()

@app.route('/request-items', methods=['POST'])
def handle_request():
    data = request.get_json()
    table = data.get("table")
    items = data.get("items", {})
    call_staff = data.get("callStaff", False)
    print(f"[RECEIVED] Table: {table}, Items: {items}, Call Staff: {call_staff}")
    request_queue.put((table, items, call_staff))

    return jsonify({"status": "received"})

def run_flask():
    app.run(port=9000)

# 진입점
if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    tkinter_mainloop()
