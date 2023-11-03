import os

path = input('\n\nNote : All the files in the folder will be passing through this program\nenter the path folder  = ')

path = path.replace('\\', '/') + '/'

print(path)


def f(fullfilename):  # function returns a modified file name where singer
                      # name and song name are interchanged
    fileextn = fullfilename.split('.')[-1]
    filename = fullfilename.split("."+fileextn)[0]
    singername, songname = filename.split(' - ')[:-1], filename.split(' - ')[-1]
    singername = '-'.join(i for i in singername)
    newname = songname + ' - ' +singername
    return newname+'.'+fileextn


for i in os.listdir(path):
    os.rename(path + i, path + f(i))
    print(f(i))
print('\nThese are the new file names\nyour filenames are changed.\nplease check in the folder')
