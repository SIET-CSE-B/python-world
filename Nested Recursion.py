def eval_expr(expr):
    if isinstance(expr, int):
        return expr
    op, left, right = expr
    if op == '+':
        return eval_expr(left) + eval_expr(right)
    elif op == '*':
        return eval_expr(left) * eval_expr(right)

# Test
expr = ['*', ['+', 2, 3], 4]  # (2 + 3) * 4 = 20
print("Result:", eval_expr(expr))
