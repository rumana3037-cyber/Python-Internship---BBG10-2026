#1.Create my_story.txt and write three lines.

with open("my_story.txt", "w") as file:
    file.write("I want to build automation scripts with Python.\n")
    file.write("I want to become confident in backend web development.\n")
    file.write("I want to solve real-world problems cleanly using code.\n")
    
#2.Read my_story.txt line by line and print each line with its character count.

with open("my_story.txt", "r") as file:
    for line in file:
        clean_line = line.strip()
        print(f"{clean_line} -> Length: {len(clean_line)}")
        
        
#3.Append a fourth line containing "2026-07-22" to my_story.txt.

with open("my_story.txt", "a") as file:
    file.write("2026-07-22\n")

# Verify original content is intact
with open("my_story.txt", "r") as file:
    print(file.read())  
    
    
#4.Copy contents of input.txt into copy.txt

with open("input.txt", "r") as source_file:
    data = source_file.read()

with open("copy.txt", "w") as target_file:
    target_file.write(data)

print("File copied successfully!")

#5.Count total number of words in a text file.

with open("my_story.txt", "r") as file:
    text = file.read()
    words = text.split()
    print(f"Total words: {len(words)}")
  