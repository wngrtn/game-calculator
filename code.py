from typing import List, Literal, Optional, Tuple
from operator import add, sub, mul, truediv, mod, pow 

Token = str
Tree = list
Operator = Literal['+', '-', '*', '/', '%', '^']

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '%': mod,
    '^': pow,
}


class TokenizationError(ValueError):
    pass


class EvaluationError(ValueError):
    pass


def _tokenize(expression: str) -> List[Token]:

    tokens: List[Token] = []

    current_token = ''

    for i, char in enumerate(expression):

        if char == ' ':
            continue

        if char in ['+', '-'] and current_token in ['+', '-']:
            raise TokenizationError(f'Cannot tokenize after {expression[:i]}')

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
            raise TokenizationError(f'Too many . at {expression[:i]}')

        if char == '.':
            current_token += char
            continue

        raise TokenizationError(f'Illegal character at {expression[:i+1]}')

    tokens.append(current_token)

    return tokens


def _split_token_list(
    tokens: List[Token],
    operator: Operator,
) -> Optional[Tuple[List[Token], List[Token]]]:

    if operator in tokens:
        i = tokens.index(operator)
        return tokens[:i], tokens[i+1:]


def _evaluate(tokens: List[Token]) -> Tree:

    for operator in OPERATORS:

        tokens_split = _split_token_list(tokens, operator)

        if tokens_split:
            left, right = tokens_split

            return OPERATORS[operator](_evaluate(left), _evaluate(right))

    if len(tokens) > 1:
        raise EvaluationError(f'Cannot find operator in {tokens}')

    try:

        return float(tokens[0])

    except ValueError:

        raise EvaluationError(f'Cannot convert {tokens[0]} to float.')


def calculate(expression: str) -> float:

    return _evaluate(_tokenize(expression))

