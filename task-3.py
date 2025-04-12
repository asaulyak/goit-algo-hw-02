pairs = {
    '{': '}',
    '}': '{',
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
}

def is_symmetric(string: str):
    stack = []

    for symbol in string:
        if pairs.get(symbol):
            top = stack[-1] if len(stack) > 0 else None
            pair = pairs.get(top)

            if symbol == pair:
                stack.pop()
            else:
                stack.append(symbol)

    return len(stack) == 0

while True:
    expression = input('Type expression: ')
    symmetric = is_symmetric(expression)

    print(f'Is symmetric: {symmetric}')
