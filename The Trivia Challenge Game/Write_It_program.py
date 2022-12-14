# Write It
# Demonstrates writing to a text file

print("Creating a text file with the write() method.")
text_file = open("write_it_one.txt", "w")

text_file.write("line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")

text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it_one.txt", "r")
print(text_file.read())
text_file.close()

print("\nCreating a text file with the writelines() method.")
text_file = open("write_it_two.txt", "w")

lines = ["Lines 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it_two.txt", "r")
print(text_file.read())
text_file.close()

input("\n\nPress the enter key to exit.")