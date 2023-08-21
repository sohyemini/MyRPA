
read_f = open(r".\E007_watchdog.py", 'r')
write_f = open(r"..\files\copied_watchdog.py", 'w', encoding="utf-8")

txt = """
    # 이 파일은 copy를 한 것이 아니고
    # 원본 파일을 한줄씩 읽어서 사본파일에 한줄씩 쓴 결과입니다.
"""
write_f.write(txt)

while True:
    line = read_f.readline()
    if not line:
        break
    else:
        write_f.write(line)
        print(line, end="")

read_f.close()
write_f.close()