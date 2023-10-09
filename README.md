# PwnedChecker
PwnedChecker allows you to check if your password has been compromised in any data breaches by leveraging the HaveIBeenPwned API. It creates a SHA-1 hash of the password, and sends a request using the first five characters of the hash to the API, and processes the response to determine if the password has been pwned.

# Key Features:
Password Hashing: Utilizes 'hashlib' for SHA-1 hashing algorithm to securely hash the user's password.

API Integration: Makes use of the HaveIBeenPwned's API to verify if the password has been exposed in data breaches.

Response Processing: Parses the API response to find the complete hash and retrieve the count of breaches.

User-Friendly Interaction: Guides the user through the process with clear prompts and informative messages.

# Usage:
Clone the repository or download the Python script.

Run the script in a terminal and follow the prompts to input your password.

The program will hash your password, check for breaches, and display the results.

# Usage Example:

Without command-line argument '--show-hash':

![image](https://github.com/SriharC/Password-Breach-Checker/assets/42175655/e66e4d7b-3db8-4911-af03-7c1a8d771cc1)


With command-line argument '--show-hash':

![image](https://github.com/SriharC/Password-Breach-Checker/assets/42175655/fea5f5bb-f74e-41f8-9099-7bef507a5838)
