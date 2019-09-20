import os, sys

# inFolder = input('drag and drop the folder: \n')
# inFolder = inFolder.replace("\\", "").replace(" ", "\ ")
# print(inFolder)
#

if __name__ == '__main__':
    for arg in sys.argv:
        # next: permettere la ricezione di più cartelle in input
        pass

    if sys.argv[1]:
        path = sys.argv[1]
    else:
        path = input('drag and drop the folder: \n')

    print(path)

    print(os.path.exists(path))

    os.chdir(path)

    files = os.listdir(path)

    for file in files:
        print(file)

        rename = file.replace('+', ' ')

        print(rename)

        os.rename(file, rename)