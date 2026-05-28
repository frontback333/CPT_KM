import os

def getfile(path):
    fdict = {}

    with os.scandir(path) as entries:
        for file in entries:
            if file.is_file():
                with open(file.path, "r", encoding="utf-8", errors="ignore") as f:
                    fcontent = f.read()

                fdict[file.name] = (file.stat().st_size, fcontent)
    return fdict

def compareDir(dir1, dir2):
    dir1files = getfile(dir1)
    dir2files = getfile(dir2)
    
    if len(dir1files) != len(dir2files):
        print("파일수 불일치")
    else:
        print("파일수 일치")
        
    print("dir1 순회")
    for file_name, info1 in dir1files.items():
        if file_name not in dir2files:
            print(dir2 + "에 " + file_name + "없음")
        else:
            print(dir1 + ',' + dir2 + "에 모두 " + file_name + "있음")
            info2 = dir2files[file_name]
            if info1[1] != info2[1]:
                print(file_name + " 크기 불일치")
            else:
                print(file_name+ "크기 일치")
            if info1[2] != info2[2]:
                print(file_name + " 내용 불일치")
            else:
                print(file_name + "내용 일치")

    print("dir2 순회")
    for file_name, info2 in dir2files.items():
        if file_name not in dir1files:
            print(dir1 + "에 " + file_name + "없음")   
        
    print("일치")

dir1 = input()
dir2 = input()
compareDir(dir1,dir2)