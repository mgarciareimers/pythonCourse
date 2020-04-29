from readers import standard, rudimentary

file_path = './files/test.txt'

# Rudimentary read.
# print('*** Rudimentary ***')
# rudimentary.read(file_path)
# print('*** End Rudimentary ***\n')

# Standard read.
print('*** Standard ***')
standard.read(file_path)
print('*** End Standard ***')

# In case of running the program in both Linux/MacOS and Windows, since path system is different, a library has been
# created to solve the problem: pathlib (find more in https://docs.python.org).
