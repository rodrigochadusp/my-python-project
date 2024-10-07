import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True):
    """Generates a random password of specified length."""

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return sum(numbers) / len(numbers)

def reverse_string(text):
    """Reverses a given string."""
    return text[::-1]



def main():
    """Main function to demonstrate the functionalities."""
    password = generate_password()
    print(f"Generated Password: {password}")

    numbers = [1, 2, 3, 4, 5]
    average = calculate_average(numbers)
    print(f"Average: {average}")

    text = "hello"
    reversed_text = reverse_string(text)
    print(f"Reversed String: {reversed_text}")

if __name__ == "__main__":
    main()
