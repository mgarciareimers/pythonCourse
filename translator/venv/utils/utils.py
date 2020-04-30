from translate import Translator
from os import remove


# Method that translates the input string to a language.
def custom_translator(string, language):
    return Translator(from_lang='es-ES', to_lang=language).translate(string)


# Method that removes a file.
def remove_file(path):
    try:
        remove(path)
    except FileNotFoundError:
        pass
