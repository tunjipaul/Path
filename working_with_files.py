from pathlib import Path
#setting up 
paulspace = Path("paulspace_files")
paulspace.mkdir(exist_ok= True)
file_path = paulspace/"notes.txt" 
file_path

# #create a file 
# #creating with "w"and "x", w - write creates the file if it does not exist, overwrite it if it does.
# #while x- exclusive create, creates the file only if it does not exist, errors if it does. (safe if you don't want to overwrite by mistake).
# #use w when you are okay with replacing old content, use x when you want to avoid accidental overwrites.

# #create or overwrite using 'w
# # # f = open(file_path, "w", encoding = "utf-8")
# # # f.write("this is the first line in notes.txt\n")
# # # f.close()

# # # # safe -create using 'x' (uncomment to try once)
# # # f = open(paulspace / "created_on.txt", "x", encoding ="utf-8")
# # # f.write("this file will only be created if it does not exist.\n")
# # # f.close()

# # #open a file.
# # #opening a file prepares it for reading or writing.

# # #open for writing again.
# # f = open(file_path, "w", encoding= "utf-8")
# # f.write("replace the old content with this line.\n")
# # f.close()

# # #write to a file.
# # #writing puts text into the file. write() does not add newlines automaatically( you add\n yourself)

# # f = open(file_path, "w", encoding = "utf-8")
# # f.write("shopping list:\n")
# # f.write(" - rice\n")
# # f.write("- beans\n")
# # f.write("- garri\n")
# # f.close()

# # #append to a file append adds to the end without deleting what's already there.

# # f = open(file_path, "a", encoding = "utf-8")
# # f.write(" - groundnut oil\n")
# # f.write(" - maggi\n")
# # f.close()


# #read from a file.
# #there are 4 common ways:
# #read()- whole file as one string.
# #read(n) - first n characters.
# # readline() - one line
# # readlines() - list of all lines

# #read the whole file
# # f = open(file_path, "r", encoding = "utf-8")
# # content = f.read()
# # f.close()
# # print(content)

# # #read line by line
# # f =open(file_path, "r", encoding="utf-8")
# # print("first line:", f.readline().rstrip())
# # print("second line:", f.readline().rstrip())
# # f.close()

# read as a list of lines. 
# f = open(file_path, "r", encoding = "utf-8")
# lines = f.readlines()
# f.close()
# print("lines list:", [line.rstrip() for line in lines])

#iterate over lines, (memory friendly)
# f= open(file_path, "r", encoding = "utf-8")
# for line in f:
#     print("->", line.rstrip())
# f.close()

# #close the file.
# #always close files opened with open(...).
# #it flushes (saves) any buffered data to disk.
# # it releases the OS handle so other programs can use the file.
# # #it avoids weird bugs (especially on windows)

# # #you have seen f.close() above. but there's a better way...

# # #8. use with open(...) as f: (best practice)
# # the with statement automatically closes the file even if an error happens. 
# this is the recommended way.

# #write safely 
# with open(file_path, "w", encoding = "utf-8") as f:
#     f.write("my to-do list:\n")
#     f.write(" - revise python file handling\n")
#     f.write(" - practice error handling within a function\n")
#     f.write(" - practice JSON and CSV\n")

# # #APPEND SAFELY
# with open(file_path, "a", encoding = "utf-8") as f:
#     f.write("- build a small project\n")


# with open (file_path, "r+", encoding = "utf-8") as f:
#     f.write("my to-do list:\n")
#     f.write(" - revise python file handling\n")
#     f.write(" - practice error handling within a function\n")
#     f.write(" - practice JSON and CSV\n")

# #what happens when things go wrong.
# #- Sometimes files don't exist, or we don't have permission to read them.
# #  Python will give us an error, 
# # but we can catch and handle these errors gracefully. Let's see how to do that.

# from pathlib import Path
# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok= True)
#  #try to read a file that doesn't exist.
# try:
#    with open(workspace / "missing_file.txt", "r") as f:
#       content = f.read()
#       print("file content:", content)
# except FileNotFoundError:
#     print("oops! that file does not exist yet")
#     print("let's create it first")

# #now create the file.
# with open(workspace/ "missing_file.txt", "w") as f:
#     f.write("Now i exist!")
#     print("file created successfully!")

#     #if you write this correctly, you should see something like this...

#     """
#     oops! that file does not exist yet.
#     lets create it first!
#     file created successfully!
#     """ --#True

# #checking if files exist before using them.

# #before trying to read or write files, its smart to check if they exist first.
# from pathlib import Path
# workspace = Path("workspace_files")
# file_path = workspace/"notes.txt"


# with open(file_path, "w", encoding= "utf-8") as f:
#     f.write("In the beginning was the word, and the word was with God and the word was God, In him was everything that was made and everything was made through him.")

# # #check if our file exists

# if file_path.exists():
#     print(f"found the file: {file_path.name}")
    
#      #get some information about the file.
    
#     file_size = file_path.stat().st_size
#     print(f"file size: {file_size} bytes")
    
#     #read and show the content
    
#     with open(file_path, "r", encoding ="utf-8") as f:
#         content = f.read()
#         print(f"content preview: {content[:50]}...")
        
#         #first 50 characters.

# else:
#     print(f"file {file_path.name} does not exist")
#     print("you might want to create it first!")

#     #if notes.txt exists.
#     """
#     found the file: notes.txt
#     file size: 67 bytes
#     content preview: Todo:
#     - Revise Python file handling
#     - Practice J...
#     """
#     #if notes.txt does not exist
#     """
#     file notes.txt does not exist
#     You might want to create it first!
#     """


# #working with JSON Files (Storing data)
# #json files are greaat for storing structured data liike dictionaries and lists. 
# # think of them as a way to save python data to a file.
# import json
# from pathlib import Path
# workspace = Path("workspace_files")

# #create some student data (like a mini database)
# student_data ={
#     "name": "oyindamola", 
#     "age": 16,
#     "courses": ["python", "data science", "web development"],
#     "grades": {"python": "A", "Data Science": "B+", "Web Development": "A-"},
#     "is_graduated": False
# }

# #save the data to a JSON File
# json_file = workspace / "student_data.json"
# with open(json_file, "w", encoding="utf-8") as f:
#     json.dump(student_data, f, indent=2) #indent=2 makes it pretty and readable.

# print("student data saved to JSON File!")

# # #now read it back

# with open(json_file, "r", encoding ="utf-8") as f:
#     loaded_data = json.load(f)
#     print("\n Data read from JSON file:")
#     print(f"Student name: {loaded_data['name']}")
#     print(f"age:{loaded_data['age']}")
#     print(f"courses: {", ".join(loaded_data['courses'])}")
#     print(f"python grade: {loaded_data['grades']['python']}")
#     #you use load function to read a json file.

# # working with csv files -spreadsheet like data
# #-csv files are like simple spreadsheets. 
# they are perfect for storing data in rows and columns.

# import csv
# from pathlib import Path
# workspace = Path('workspace_files')
# csv_file = workspace/'students.csv'

# #create sample student data
# students = [
#     ["name", "age", "course", "grade"], #header row
#     ["precious", 20, "python", "A"],
#     ["favour",22, "javascript", "B+"],
#     ["ore", 21, "python", "A-"],
#     ["susan", 23, "data science", "A"]
# ]

# #write data to csv file 
# with open(csv_file, "w", newline="", encoding= "utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerows(students) #write all rows at once.
# print("student data written to csv file!")

# #read the csv file back
# print("\n reading csv file:")
# with open(csv_file, "r", encoding= "utf-8") as f:
#     reader = csv.reader(f)
#     for row_number, row in enumerate(reader):
#         if row_number == 0: #header row
#             print(f"headers: {'|'. join(row)}")
#             print("-"*40)
#         else: #data rows
#             name, age, course, grade = row
#             print(f"{name} ({age} years) - {course}: {grade}")
        


# #working with multple files at once.
# # #sometimes you need to read from one file and write to another at the same time.

# from pathlib import Path
# workspace = Path("workspace_files")
# input_file = workspace/ "original.txt"
# output_file = workspace/ "processed.txt"

# #create an input file with some text
# sample_text = """hello world
# python programming
# file handling tutorial
# learning is fun
# """

# with open(input_file, "w", encoding ="utf-8") as f:
#     f.write(sample_text)

# print("created input file")

# #process the file: read from input, write processed version to output.
# with open(input_file, "r", encoding= "utf-8") as infile,\
#      open(output_file, "w", encoding= "utf-8") as outfile:

#     line_number = 1
#     for line in infile:
#         #process each line: make it uppercase and add line numbers:
#         processed_line = f"line {line_number}: {line.strip().upper()}\n"
#         outfile.write(processed_line)
#         line_number +=1
# print("file processing complete!")

# # show the results.
# print("\nOriginal File:")
# with open(input_file, "r", encoding= "utf-8") as f:
#     print(f.read())

# print("\nProcessed File:")
# with open(output_file, "r", encoding ="utf-8") as f:
#     print(f.read())

# #output to expect:
# """
# created input file
# file processing complete!

# Original file:
# hello world
# python programming
# file handling tutorial
# learning is fun

# # Processed aFile:
# # Line 1: HELLO WORLD
# # Line 2: PYTHON PROGRAMMING
# # Line 3: FILE HANDLING TUTORIAL
# # Line 4: LEARNING IS FUN.
# # """

# #Moving inside a file.
# #sometimes you want to jump to a specific part of a file instead of reading from beginning

# from pathlib import Path
# workspace = Path("workspace_files")
# file_path = workspace/"story.txt"

# # #create a smaple story file.
# story = """Once upon a time, there was lady who was very curious and inquisitive, she just want to know how things work behind the scene.
# eventually she had an opportunity to hop into the worldd of programming for the first time.
# she started with python, now she codes in python every day.
# one day, she discovered file handling.
# it opened up a whole new world of possibilities
# the end.
# """
# with open(file_path, "w", encoding= "utf-8") as f:
#     f.write(story)
# print("created a story file!")

# #now let's explore moving around in the file.
# with open(file_path, "r", encoding= "utf-8") as f:
#     print("\nFile positioning demo:")
#     #read first 20 characters.
#     first_part = f.read(20)
#     print(f"first characters: '{first_part}")
    
#     #check where we are now.
#     current_position = f.tell()
#     print(f"current position in file: {current_position}")
#     #jump to the beginning
#     f.seek(0)
#     print(f"after seeking to beginning: position {f.tell()}")
#    #jump to position 50 and read from there.
#     f.seek(50)
#     rest_of_line = f.readline()
#     print(f"reading from position 50: {rest_of_line.strip()}")

#     #go back to beginning and read the first line
#     f.seek(0)
#     first_line = f.readline()
#     print(f"first line: '{first_line.strip()}")


#     #commmon mistakes to avoid 
#     #- forgetting to close files (use with statements)
#     #- not handling the case when files don't exist.
#     #- using the wrong file mode("w" overwrites everything!)
#     #- forgetting to specify enncoding (use encoding ="utf-8")
#     #- not understanding the difference between 'r', 'w', and 'a' modes.

