#Kevin Farokhrouz
#1002072886
#Python 3.11.9 (Scripting language)
#Win 11

import os


#Uses os.path.getsize to return the size of the file at filePath
def getSize(filePath):
    return os.path.getsize(filePath) 
    
#Computes the total size, in bytes, of all of the files located in all subfolders beginning at folder
def dirSpace(folder):
    sum = 0
    #Creates a list of every entry inside of folder
    entries = os.listdir(folder)
    for entry in entries:
        #Skip . and ..
        if entry == "." or entry == "..":
            continue
        #The path to the entry is the current path + " /" + the entry name
        entry = os.path.join(folder, entry)
        #If the entry is a file, increment sum by the file's size
        if os.path.isfile(entry):
            sum += getSize(entry)
        #If the entry is a folder, recurse on the folder and increment sum by the size of all files in all subfolders beginning at entrypath
        else:
            sum += dirSpace(entry)
    return sum

#Begin recursion at cwd
sum = dirSpace(".")
print(sum)