from collections import deque
import re

def is_palindrome(string: str):
    clean_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    symbols = deque()

    symbols.extend(clean_string)

    while len(symbols) > 1:
        right = symbols.pop()
        left = symbols.popleft()

        if right != left:
            return False

    return True

while True:
    string = input('Check palindrome: ')
    palindrome = is_palindrome(string)

    print(f'Is palindrome: {palindrome}')