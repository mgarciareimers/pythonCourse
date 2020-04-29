# Rudimentary file read operation.
def read(path):
    try:
        # Open a file.
        my_file = open(path)

        # Read the file and print the content.
        # print(my_file.read())

        # Move the cursor to the first character (0).
        # my_file.seek(0)

        # Get lines.
        lines = my_file.readlines()
        print(lines)

        # Close the file to leave it free.
        my_file.close()
    except FileNotFoundError as error:
        print('File does not exist!!!')
        raise error
    except IOError as error:
        print('IO error!!!')
        raise error
