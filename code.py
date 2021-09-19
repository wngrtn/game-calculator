from operator import add, sub, mul, truediv, mod, pow 

def calculate(expression: str) -> float:

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '%': mod,
        '^': pow,
    }

    operators_padded = map(lambda x: f' {x} ', operators)

    for operator in operators_padded:
        arguments_split = expression.split(operator)
        if len(arguments_split) > 1:
            arguments_cleaned = map(float, arguments_split)
            return operators[operator.strip()](*arguments_cleaned)

    return float(arguments_split[0])
