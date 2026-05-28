import os

def listAll(path):
    dirfiles = os.listdir(path)
    subdirs = [path + "/" + x for x in dirfiles if os.path.isdir(path + "/" +x)]
    print(path)
    for subdir in subdirs:
        listAll(subdir)

def pf(loc):
    print(loc)
    for entry in os.scandir(loc):
        if entry.is_dir():
            print(f"{loc}/{entry.name}")
            pf(f"{loc}/{entry.name}")

pf("C:\\Program Files\\RPA")