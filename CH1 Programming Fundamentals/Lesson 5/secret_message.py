from os import listdir, rename 
from string import digits

def rename_files(directory):
    # get file names
    files = listdir(directory)

    # loop through files
    for file in files:
        file = directory + file
        new_name = file.translate(None, digits)
        rename(file, new_name)

rename_files('prank/')