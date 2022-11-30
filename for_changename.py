import os

old_path = "E:/gt/"
filename_list = os.listdir(old_path)

for i in filename_list:
    name = i.split('_')[0]
    if name == 'lung':
        used_name = old_path + i
        new_name = old_path + i.replace('lung_','lung-')
        os.rename(used_name, new_name)
        print(i)