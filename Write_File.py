# Create a new file by specifying the write mode "w".
aNewFile = open("myNewTextFile.txt", "w")

# Now you'll add some text to the file.
aNewFile.write("This is the first line of my text. "
"\nThis is the second line of my text. "
"\nThis is the third line of my text. ")

# Close the file
aNewFile.close()

# Now you'll open the file for reading in read mode 'r'
aNewFile = open("myNewTextFile.txt", "r")

# Read the contents of the file
textFromTheFile = aNewFile.read()

# Output the contents to the screen
print(textFromTheFile)

#Close the file
aNewFile.close()
