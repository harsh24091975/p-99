import os
import shutil
import time

def main():
    deletedfoldercount=0
    deletedfilescount=0

    path="C:\Users\Rohtas Hooda\Desktop\harsh\c99\c-99"
    days=30
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for root,folders,files in os.walk(path):
            if seconds>=get_file_or_folder(root):
                remove_folder(root)
                deletedfoldercount+=1
                break
            else:
                for folder in folders:
                    fpath=os.path.join(root,folder)
                    if seconds>=get_file_or_folder(fpath):
                        remove_folder(fpath)
                        deletedfoldercount+=1
                for file in files:
                    filepath=os.path.join(root,file)
                    if seconds>=get_file_or_folder(filepath):
                        remove_file(filepath)
                        deletedfilescount+=1
        else:
            if seconds>=get_file_or_folder(filepath):
                        remove_file(filepath)
                        deletedfilescount+=1
    else:
        print(f"'{path}' is not found")
        deletedfilescount+=1
    print(f"total folders deleted : {deletedfoldercount}")
    print(f"total files deleted : {deletedfilescount}")


def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed")
    else:
        print(f"unable to remove the "+path)

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed")
    else:
        print(f"unable to remove the "+path)

def get_file_or_folder(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()
