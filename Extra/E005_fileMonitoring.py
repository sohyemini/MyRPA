import os, time

path = "./"
file_list_org = []

if not os.path.exists(path):
    print("해당 경로가 존재하지 않아 프로그램을 종료합니다.")
    exit(0)

while True:
    file_list_new = os.listdir(path)

    # 추가되었는지 확인
    for added in file_list_new:
        if added not in file_list_org:
            print(f"added = {added}")
            file_list_org.append(added)

    # 삭젝가되었는지 확인
    for deleted in file_list_org:
        if deleted not in file_list_new:
            print(f"deleted = {deleted}")
            file_list_org.remove(deleted)


    time.sleep(1)

