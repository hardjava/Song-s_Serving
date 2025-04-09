from time import sleep

import serial
import time

# HC-05 연결 포트 및 속도
bluetooth_port = '/dev/tty.HC-05'  # 너 시스템에 맞는 포트
baud_rate = 9600

try:
    ser = serial.Serial(bluetooth_port, baud_rate)
    time.sleep(2)  # 연결 안정화 대기

    print("HC-05 연결 완료. 숫자(0~9)를 입력하세요. 'q' 입력 시 종료.")

    while True:
        user_input = input("보낼 숫자 입력 (0, 1, 2 등): ")

        if user_input.lower() == 'q':
            print("연결 종료")
            break

        ser.write(b'0')

        sleep(10)

    ser.close()

except serial.SerialException as e:
    print("블루투스 연결 실패:", e)
