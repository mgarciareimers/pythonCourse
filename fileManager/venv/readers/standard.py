# Standard way of reading files. Mode can be set as 'r' or 'w' or 'r+' or 'a'.
# r: Read.
# w: Overwrite/Create new file.
# r+: Read and substitute.
# a: Append at the end.
def read(path):
    try:
        with open(path, mode='r') as my_file:
            # text = my_file.write('hey, I am writing!\n')
            print(my_file.read())

            # In this case, there is no need to close the file since that is done with the "with open..." operation.
    except FileNotFoundError as error:
        print('File does not exist!!!')
        raise error
    except IOError as error:
        print('IO error!!!')
        raise error
