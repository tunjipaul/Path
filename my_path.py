# import os
# print("current working directory:", os.getcwd()) 

# #absolute path example.
# absolute_path = r"C:\Users\cddf\Desktop\My_Virtual_Environment\my_path.py"

# #relative path example.
# relative_path = "my_path.py"

# print("absolute path:", absolute_path)
# print("relative path:", relative_path)

# #joining the paths, the right way.

# import os 
# folder = "C:/Users/cddf/Desktop/My_Virtual_Environment"
# filename = "my_path.py"
# path = os.path.join(folder, filename)
# print("full path:", path)

# #checking if a file/folder exists
# #os.path.exists.

# import os
# path = "my_path.py"
# if os.path.exists(path):
#     print('yes, the file exists!')
# else: 
#     print("file not found")

# #using pathlib(modern way)

#python has a modern library - pathlib which is easier to use than os.
from pathlib import Path

#current working directory
print("current working directory:", Path.cwd())
#create a path project.
file = Path("New_Text_Document.txt")
#check if it exists.
print("file exists:", file.exists())

#combine paths
folder = Path("C:/Users/cddf/Desktop/My_Virtual_Environment") 

full_path = folder/"New_Text_Document.txt"
print("full path:",full_path)


#navigating folders with pathlib
from pathlib import Path
#getparent folder of current file
print("parent folder:", Path.cwd().parent)
#list all files in a directory
for file in Path.cwd().iterdir():
    print(file)