from os import listdir

def rename_files():
    # get file names
    files = listdir('prank')
    print files

rename_files()