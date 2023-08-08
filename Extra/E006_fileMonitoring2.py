import os, datetime, time

path = "./"
info_org = []
info_new = []
file_list_org = []

if not os.path.exists(path):
    print("해당 경로가 존재하지 않아 프로그램을 종료합니다.")
    exit(0)

while True:
    info_new.clear()
    file_list_new = os.listdir(path)
    for file in file_list_new:
        # 상세정보 업데이트
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        size = os.path.getsize(file)
        info_new.append((file, mtime, size))

    # 추가되었는지 확인
    for added in file_list_new:
        if added not in file_list_org:
            print(f"added = {added}")
            file_list_org.append(added)
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(added))
            size = os.path.getsize(added)
            info_org.append((added, mtime, size))

    # 삭젝가되었는지 확인
    for deleted in file_list_org:
        if deleted not in file_list_new:
            print(f"deleted = {deleted}")
            file_list_org.remove(deleted)
            for del_data in info_org:
                if del_data[0] == deleted:
                    info_org.remove(del_data)

    for org in info_org:
        if org not in info_new:
            try:
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(org[0]))
                size = os.path.getsize(org[0])
                info_org.append((org[0], mtime, size))
                print(f"modified = {org[0]}")
            except:
                print(f"file deleted already = {org[0]}")
            info_org.remove(org)

    time.sleep(1)


