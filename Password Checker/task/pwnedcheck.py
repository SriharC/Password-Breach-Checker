import hashlib
import requests
import argparse


def password_input():
    global user_password
    while True:
        user_password = input("Enter your password (or 'exit' to quit): ")
        if user_password.lower() == 'exit':
            print("Goodbye!")
            return None
        elif len(user_password) < 8:
            return "Your password is too short. Please enter a password of at least 8 characters."
        else:
            return user_password


def password_hash(user_password):
    global sha_hash
    sha_hash = hashlib.sha1(user_password.encode('utf-8')).hexdigest()
    return sha_hash


def pass_checker(sha_hash):
    params = {
        'Add-Padding': True,
    }
    hash_string = '{}'.format(sha_hash)
    first_five = []
    for x in range(0, 5):
        first_five.append(hash_string[x])
    five_join = "".join(first_five)
    api_url = "https://api.pwnedpasswords.com/range/{}".format(five_join)
    response = requests.get(api_url, params=params)
    print("Checking...")
    return response


def pwned_response(response, sha_hash, show_hash):
    if response.status_code == 200:
        response_text = response.text
        complete_hash = sha_hash.upper()[5:]
        count = 0
        for line in response_text.split('\n'):
            if line.startswith(complete_hash):
                count = int(line.split(':')[1])
                break
        if show_hash:
            print("Your hashed password is: " + sha_hash)
        if count > 0:
            print("Your password has been pwned! The password \"{}\" appears {} times in data breaches.".format(str(user_password), count))
        else:
            print("Good news! Your password hasn't been pwned.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password breach checker")
    parser.add_argument("--show-hash", action="store_true", help="Show the hashed password")
    args = parser.parse_args()

    while True:
        user_password = password_input()
        if user_password is None:
            break
        sha_hash = password_hash(user_password)
        response = pass_checker(sha_hash)
        pwned_response(response, sha_hash, args.show_hash)
