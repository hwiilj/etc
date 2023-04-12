# 해당 파일리스트의 파일들을 읽어 루트부터 디렉토리 카운팅하는 코드
import os

file_tree = {}
def find_files_in_directory(file_list):
    for file in file_list:
        for root, dirs, files in os.walk('ROOT_DIR'):
            if file in files:
                loc = os.path.join(root, file)

                loc = loc[len("ROOT_DIR"):]
                index = loc.find("/")
                while index != -1:
                    if loc[:index] in file_tree:
                        file_tree[loc[:index]] = file_tree[loc[:index]] + 1
                    else:
                        file_tree[loc[:index]] = 1
                    index = loc.find("/", index + 1)
                #print(f"{file} is located in {loc}")
                break
        else:
            print(f"{file} was not found in any directories.")

file_list = []
with open("TBD_lists.txt", "r") as f:
    for line in f.readlines():
        print(line)
        line.strip()
        lb = line.find('"')
        rb = line.rfind('"')
        if lb == -1:
            continue
        file_list.append(line[lb+1:rb])

print(len(file_list))
find_files_in_directory(file_list)
file_tree = sorted(file_tree.items(), key=lambda x: x[1], reverse=True)
with open("Tree_counts.txt", "w") as f:
    for item in file_tree:
        f.write(item[0] + ":" + str(item[1]) + "\n")


