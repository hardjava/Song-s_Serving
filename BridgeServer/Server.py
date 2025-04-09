from flask import Flask, request, jsonify
import tkinter as tk
import threading
import queue

# Flask 서버 초기화
app = Flask(__name__)

# 요청 저장용 Queue
request_queue = queue.Queue()

# Tkinter 팝업 함수 (메인 스레드 전용)
def tkinter_mainloop():
    root = tk.Tk()
    root.withdraw()  # 메인 창 숨김

    def check_queue():
        try:
            table, items, call_staff = request_queue.get_nowait()

            # 팝업 창 생성
            popup = tk.Toplevel()
            popup.title("서빙 요청")
            popup.geometry("400x400")

            tk.Label(popup, text=f"🧾 {table}번 테이블 요청", font=("Arial", 16)).pack(pady=10)
            for item, count in items.items():
                if count > 0:
                    tk.Label(popup, text=f"{item.capitalize()}: {count}개", font=("Arial", 12)).pack()
            if call_staff:
                tk.Label(popup, text="🧑‍🍳 직원 호출됨!", font=("Arial", 14), fg="red").pack(pady=10)

            def on_confirm():
                print(f"[INFO] 로봇 출동 - Table {table}, Items: {items}, Staff Call: {call_staff}")
                popup.destroy()

            tk.Button(popup, text="로봇 출동하기", command=on_confirm, font=("Arial", 12)).pack(pady=20)

        except queue.Empty:
            pass
        root.after(500, check_queue)  # 주기적으로 큐 확인

    check_queue()
    root.mainloop()

# Flask 라우트
@app.route('/request-items', methods=['POST'])
def handle_request():
    data = request.get_json()
    table = data.get("table")
    items = data.get("items", {})
    call_staff = data.get("callStaff", False)

    print(f"[RECEIVED] Table: {table}, Items: {items}, Call Staff: {call_staff}")

    # ❗ 메인 루프에 전달
    request_queue.put((table, items, call_staff))

    return jsonify({"status": "received"})

# Flask 실행은 별도 스레드로
def run_flask():
    app.run(port=9000)

# 진입점
if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    tkinter_mainloop()  # 메인 스레드는 Tkinter가 독점
