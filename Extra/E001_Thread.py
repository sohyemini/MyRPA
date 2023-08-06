import threading
import time

def doingJob(_id, _duration):
    while True:
        time.sleep(_duration)
        print(f"Doing Something {_id}")

# 쓰레드1 생성
thread1 = threading.Thread(target=doingJob, args = ('RPA', 1))
thread1.start()
print("쓰레드 1 시작됨")

# 쓰레드2 생성
thread2 = threading.Thread(target=doingJob, args = ('Process Automation', 0.5))
thread2.start()
print("쓰레드 2 시작됨")

print("5초 Sleep 호출")
time.sleep(5)
print("메인 쓰레드 종료")
