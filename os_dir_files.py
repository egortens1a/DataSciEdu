import os

os.chdir(r"C:\Users\PC\Desktop\main")
res = []
for current_dirs, dirs, files in os.walk("."):
    print(current_dirs, dirs, files)
    for file in files:
        if '.py' in file:
            res += ['main' + current_dirs[1:]]
            break
out = open("result.txt", 'w')
for j in res:
    out.write(j + '\n')

print(os.getcwd())
