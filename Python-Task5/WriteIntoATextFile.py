#writing the files

writeFile = open("text_file.txt", "w")
string = input("Enter a string:")
writeFile.write(string)
writeFile.close()

#reading the files

readFile = open("text_file.txt")
print(readFile.readline())
