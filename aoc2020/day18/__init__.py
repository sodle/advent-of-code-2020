def evaluate_expression(expr: str) -> int:
    while "(" in expr:
        l_parens = 1
        r_parens = 0

        open_paren_idx = expr.index("(")
        idx = open_paren_idx + 1
        while l_parens != r_parens:
            if expr[idx] == "(":
                l_parens += 1
            elif expr[idx] == ")":
                r_parens += 1
            idx += 1

        paren_value = evaluate_expression(str(expr[open_paren_idx + 1:idx - 1]))
        expr = f"{expr[:open_paren_idx]}{paren_value}{expr[idx:]}"

    expr = expr.split(" ")
    while len(expr) > 1:
        a, operator, b = expr[:3]
        if operator == "+":
            value = int(a) + int(b)
        else:
            value = int(a) * int(b)
        expr = [value, *expr[3:]]

    return expr[0]


def evaluate_expression_part2(expr: str) -> int:
    while "(" in expr:
        l_parens = 1
        r_parens = 0

        open_paren_idx = expr.index("(")
        idx = open_paren_idx + 1
        while l_parens != r_parens:
            if expr[idx] == "(":
                l_parens += 1
            elif expr[idx] == ")":
                r_parens += 1
            idx += 1

        paren_value = evaluate_expression_part2(str(expr[open_paren_idx + 1:idx - 1]))
        expr = f"{expr[:open_paren_idx]}{paren_value}{expr[idx:]}"

    expr = expr.split(" ")
    while "+" in expr:
        oper_idx = expr.index("+")
        a = int(expr[oper_idx - 1])
        b = int(expr[oper_idx + 1])
        result = a + b
        expr = [*expr[:oper_idx - 1], result, *expr[oper_idx + 2:]]
    while "*" in expr:
        oper_idx = expr.index("*")
        a = int(expr[oper_idx - 1])
        b = int(expr[oper_idx + 1])
        result = a * b
        expr = [*expr[:oper_idx - 1], result, *expr[oper_idx + 2:]]

    return expr[0]


def part1(expressions: [str]) -> int:
    return sum(evaluate_expression(expr) for expr in expressions)


def part2(expressions: [str]) -> int:
    return sum(evaluate_expression_part2(expr) for expr in expressions)
