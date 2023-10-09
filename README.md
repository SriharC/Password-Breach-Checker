# Password-Breach-Checker
This Python script allows you to check if your password has been compromised in any data breaches by leveraging the HaveIBeenPwned API. It creates a SHA-1 hash of the password, and sends a request using the first five characters of the hash to the API, and processes the response to determine if the password has been pwned.

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

Without command-line argument '--show-hash'
![image](https://github.com/SriharC/Password-Breach-Checker/assets/42175655/2382c7a6-121d-41ad-8854-19a0e82c6dfd)

With command-line argument '--show-hash'
![image](https://github.com/SriharC/Password-Breach-Checker/assets/42175655/6bf9d798-65f3-4b0a-8a83-5b6bca8dd6c6)
