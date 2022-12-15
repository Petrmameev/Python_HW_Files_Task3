import os

FILE_LOG_DIR = 'folder'
ROOT_PATH = os.getcwd()
full_path = os.path.join(ROOT_PATH, FILE_LOG_DIR)
list_files = []
for files in os.listdir(full_path):
    list_files.append(files)
print(list_files)
a = {}
for file in list_files:
    with open(os.path.join(ROOT_PATH, FILE_LOG_DIR, file), 'r', encoding='utf-8') as f:
        count = 0
        b =[]
        for line in f:
            count += 1
            b.append(line)
            a[file] = [count, b]
with open('finish_file.txt', 'w'):
    pass
print(a)
while a != {}:
    for k, v in a.items():
        min_text = min(a.values())
        if v == min_text:
            n = v[1][0:]
            with open('finish_file.txt', 'a', encoding='utf-8') as d:
                d.write(f'{k} \n{v[0]}\n')
                d.writelines(n)
                d.write('\n\n')
                del a[k]
                break