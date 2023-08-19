import shutil, os, zipfile

# .\res 폴더를 zip으로 압축합니다.
shutil.make_archive('rpa_d', 'zip', "..\\res")

if not os.path.exists(r'.\zip'):
    os.mkdir(r'.\zip')
    print("폴더를 만들었습니다.")
else:
    print("zip 폴더가 존재한니다.")

shutil.make_archive('.\\zip\\rpa_d', 'tar', "..\\res")

shutil.move('.\\rpa_d.zip', '.\\zip\\rpa_d.zip')
shutil.unpack_archive('.\\zip\\rpa_d.zip', '.\\zip', 'zip')

if not os.path.exists(r'.\zip\tar'):
    os.mkdir(r'.\zip\tar')
    print("tar 폴더를 만들었습니다.")
else:
    print("tar 폴더가 존재한니다.")
shutil.unpack_archive('.\\zip\\rpa_d.tar', '.\\zip\\tar', 'tar')

extract_fname = None

with zipfile.ZipFile(".\\zip\\file_zip.zip", 'w') as my_zip:
    f_list = os.listdir(".\\")
    for f in f_list:
        if os.path.splitext(f)[1] == '.py':
            my_zip.write(f)
            if extract_fname == None:
                extract_fname = f
                print(f"첫번째 파일 = {f}")

zip = zipfile.ZipFile(".\\zip\\file_zip.zip")
lst = zip.namelist()
print(f"압축파일내에 있는 파일들 \n{lst}")

os.chdir(r".\zip")
zipfile.ZipFile(".\\file_zip.zip").extract(extract_fname)
