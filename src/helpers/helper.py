import string
import random


def create_random_data(length=10, digits=True, letters=True):
    """Create random data consisting of letters/digits of the given length."""
    characters = ""
    if digits:
        characters += string.digits
    if letters:
        characters += string.ascii_letters

    random_data = "".join(random.choice(characters) for _ in range(length))

    return random_data
