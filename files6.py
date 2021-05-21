#To delete a file
#import os module and run its os.remove()
'''import os
os.remove("file1.txt")'''
#check if file exists then delete it
import os 
if os.path.exists("file3.txt"):
    os.remove("file3.txt")
else:
    print("this file doesn't exists")

#can delete only empty folders
#delete entire folder,use os.rmdir()
'''import os'''
os.rmdir("myfolder")
