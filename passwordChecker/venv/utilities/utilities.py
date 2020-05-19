import requests
import hashlib


# Method that requests the api data.
def request_api_data(password):
    # SHA1 hashed password.
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    url = f'https://api.pwnedpasswords.com/range/{ hashed_password[:5] }'  # Send only first 5 characters of the hashed password.
    response = requests.get(url)

    return response if response.status_code == 200 else None


# Method that reads the response of the API.
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hashed_string, count in hashes:
        if hash_to_check.upper() == hashed_string.upper():
            return count
    return 0


# Method that checks if the password exists in the api data.
def check_password_count(password, api_data):
    # SHA1 hashed password.
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    return get_password_leaks_count(api_data, hashed_password[5:])
