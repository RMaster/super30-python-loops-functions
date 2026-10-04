# Q11: Password Retry System
# Why a while loop? We repeat "ask for the password" until a condition changes:
# either the user gets it right or the attempts run out. The number of
# repetitions is not fixed (it could be 1, 2, or 3), so while fits.

PASSWORD = "Super30@123"   # predefined password
MAX_ATTEMPTS = 3

attempts = 0
logged_in = False

while attempts < MAX_ATTEMPTS:
    entered = input("Enter password: ")

    if entered == PASSWORD:
        logged_in = True
        break                       # correct password, leave the loop early

    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Incorrect password. {remaining} attempt(s) left.")

if logged_in:
    print("Login successful. Welcome!")
else:
    print("Account Locked")