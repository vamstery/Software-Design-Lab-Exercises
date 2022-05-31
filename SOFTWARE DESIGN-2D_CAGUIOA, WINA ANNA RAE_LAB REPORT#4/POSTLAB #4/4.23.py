import os
def find(filename):
    paths = os.listdir(filename)
    allFiles=list()
    for entry in paths:
        fullPath = os.path.join(filename, entry)

        if os.path.isdir(fullPath):
            allFiles = allFiles + find (fullPath)
        else: 
            allFiles.append(fullPath)
    
    return allFiles 

def main():
    
    filename= 'C:\kivymd\KivyMD'
    paths = find(filename)

    for elem in paths:
        print(elem)

    paths = list()
    for(dirpath,dirnames,filenames) in os.walk(filename):

        paths += [os.path.join(dirpath,file) for file in filenames]

        for elem in paths:
                print(elem)

if __name__ =="__main__":
    main()
