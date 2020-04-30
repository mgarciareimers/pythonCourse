from utils import utils

path = './files/spanish.txt'
translated_path = './files/english.txt'

try:
    with open(path, mode='r') as my_file:
        utils.remove_file(translated_path)

        with open(translated_path, mode='a') as translated_file:
            lines = my_file.readlines()
            translated_text = ''

            for line in lines:
                translated_text = f'{ utils.custom_translator(line, "en") }\n'
                translated_file.write(translated_text)

except FileNotFoundError as error:
    print('File does not exist!!!')
    raise error
except IOError as error:
    print('IO error!!!')
    raise
