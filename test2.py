def create_file():
    file = open("dili.txt", "a")
    for x in range(1, 12):
        file.write(str(x) + '\n')
create_file()

