f = open("test.txt", "w")  # Open the file for writing
f.write("first line of file \n")  # Write a line in the file
f.write("second line of file \n")  # Write another line in file
f.close()
f = open("test.txt")  # Reopen the file for reading
content = f.read()  # Read all the contents of the file
print(content)
f.close()  # Close the file
