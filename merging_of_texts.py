import os

current = os.getcwd()
folder = 'files'
file_path = os.path.join(current, folder)
files = os.listdir(file_path)

file_dict = {}
for f in files:
    full_path = os.path.join(file_path,f)
    with open(full_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        text = []
        len_text = len(lines)
        for line in lines:
            text.append(line.strip())
        file_dict[f] = (len_text, text)

sorted_values = sorted(file_dict.values())

sorted_dict = {}

for value in sorted_values:
    for key in file_dict.keys():
        if file_dict[key] == value:
            sorted_dict[key] = file_dict[key]
            break

with open('result.txt', 'w', encoding='utf-8') as file:
    for key, value in sorted_dict.items():
        file.write(f'{key}\n')
        file.write(f'{value[0]}\n')
        for val in value[1]:
            file.write(f'{val}\n')