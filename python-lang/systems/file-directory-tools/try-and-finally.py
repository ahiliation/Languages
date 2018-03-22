file = open("data.txt", 'r')
try:
    for line in file:
        print line
finally:
    file.close()
