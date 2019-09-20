import os
import sys
import traceback

if __name__ == '__main__':
    for arg in sys.argv:
        # next: permettere la ricezione di più cartelle in input
        pass

    try:
        path = sys.argv[1]
    except IndexError:
        path = input('drag and drop the folder: \n')
        path = path.replace('\\', '')
        path = path[:-1]
    except Exception:
        traceback.print_exc()

    print(path)
    print(os.path.exists(path))

    os.chdir(path)

    files = os.listdir(path)

    for file in files:
        print(file)
        if '+' in file:
            rename = file.replace('+', ' ')
            print(rename)
            os.rename(file, rename)
