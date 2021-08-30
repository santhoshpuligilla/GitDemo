file = open('test.txt')

for line in file.readlines():
    print(line)

file.close()
