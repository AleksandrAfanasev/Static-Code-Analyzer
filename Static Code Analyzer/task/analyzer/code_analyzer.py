file_path = input()
cnt = 0
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        cnt += 1
        if len(line) > 79:
            print(f'Line {cnt}: S001 Too long')
