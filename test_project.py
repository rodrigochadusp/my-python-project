import project
import pytest
import string

def test_generate_password():
    password = project.generate_password(length=8, include_digits=False, include_symbols=False)
    assert len(password) == 8
    assert password.isalnum()  # Check if it contains only letters and numbers
    assert not any(char.isdigit() for char in password) # Check no digits
    assert not any(char in string.punctuation for char in password) # Check no symbols

    password_with_digits = project.generate_password(length=8, include_digits=True, include_symbols=False)
    assert any(char.isdigit() for char in password_with_digits)

    password_with_symbols = project.generate_password(length=8, include_digits=False, include_symbols=True)
    assert any(char in string.punctuation for char in password_with_symbols)


def test_calculate_average():
    assert project.calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert project.calculate_average([]) == 0  # Test empty list
    assert project.calculate_average([0, 0, 0]) == 0
    assert project.calculate_average([-1, 1]) == 0



def test_reverse_string():
    assert project.reverse_string("hello") == "olleh"
    assert project.reverse_string("") == ""  # Test empty string
    assert project.reverse_string("12345") == "54321"
    assert project.reverse_string("racecar") == "racecar"  # Test palindrome
