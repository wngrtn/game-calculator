from typing import List
from operator import add, sub, mul, truediv, mod, pow 


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '%': mod,
    '^': pow,
}


class TokenizeError(ValueError):
    pass


def _tokenize(expression: str) -> List[str]:

    tokens: List[str] = []

    current_token = ''

    for i, char in enumerate(expression):

        if char == ' ':
            continue

        if char in ['+', '-'] and current_token in ['+', '-']:
            raise TokenizeError(f'Cannot tokenize after {expression[:i]}')

        if char in OPERATORS and current_token:
            tokens.append(current_token)
            tokens.append(char)
            current_token = ''
            continue

        if char in ['+', '-'] and not current_token:
            current_token = char
            continue

        if char.isdigit():
            current_token += char
            continue

        if char == '.' and '.' in current_token:
            raise TokenizeError(f'Not expecting another . at {expression[:i]}')

        if char == '.':
            current_token += char
            continue

        raise TokenizeError(f'Illegal character at {expression[:i]}')

    tokens.append(current_token)

    return tokens


def calculate(expression: str) -> float:

    operators_padded = map(lambda x: f' {x} ', OPERATORS)

    for operator in operators_padded:
        arguments_split = expression.split(operator)
        if len(arguments_split) > 1:
            arguments_cleaned = map(float, arguments_split)
            return OPERATORS[operator.strip()](*arguments_cleaned)

    return float(arguments_split[0])
