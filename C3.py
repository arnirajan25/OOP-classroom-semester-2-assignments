'''C3.Create two custom exceptions PasswordTooShortError' and 'PasswordTooWeakError both inheriting from a common base exception called 'PasswordError. Write a function that validates a password and raises the appropriate error.'''
class PasswordError(Exception):
    pass

class PasswordTooShortError(PasswordError):
    pass

class PasswordTooWeakError(PasswordError):
    pass

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters.")

    has_letter = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    if not (has_letter and has_digit):
        raise PasswordTooWeakError(
            "Password must contain both letters and digits."
        )

    print("Password is valid.")

try:
    pwd = input("Enter your password: ")
    validate_password(pwd)

except PasswordError as e:
    print("Error:", e)
