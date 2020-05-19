from utilities import utilities
import sys
import hashlib

print('* Welcome to the Password Checker.')

# Input password.
password = input('  Please type the password you want to check: ')

# Get the API data.
api_data = utilities.request_api_data(password)

# Check if the response is correct.
if api_data is None:
    sys.exit('  An unexpected error occurred while requesting the api data.')

# Count number of times the password is in the API data.
count = utilities.check_password_count(password, api_data)

# Show message.
if count:
    print(f'  ❌ The password has been found { count } times. You should probably user another password.')
else:
    print(f'  ✅ The password has not been found. Carry on!')
print('* Thank you for using the Password Checker')
