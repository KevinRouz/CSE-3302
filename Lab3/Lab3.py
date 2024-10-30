FILENAME = "input_RPN.txt"

def add(op1, op2):
    return op1 + op2

def mult(op1, op2):
    return op1 * op2

def sub(op1, op2):
    return op1 - op2

def div(op1, op2):
    if op2 == 0:
        raise ValueError(f"Divide by zero.")
    return op1 / op2

def square(op1):
    return op1 * op1

def rpn_eval(rpn):
    binary = {"+": add, "-": sub, "/": div, "*": mult}
    unary = {"^": square} # NEW OPERATOR! Operator ^ is a unary operator, that squares its operand.

    stack = []
    for token in rpn.split():
        if token not in binary and token not in unary:
            stack.append(float(token))
        elif token in binary:
            if len(stack) < 2:
                raise ValueError(f"Invalid expression: {rpn}, binary operators need two operands.")
            op2 = stack.pop()
            op1 = stack.pop()
            operator = binary[token]
            stack.append(operator(op1, op2))
        elif token in unary:
            op1 = stack.pop()
            operator = unary[token]
            stack.append(operator(op1))
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) > 1:
        raise ValueError(f"Invalid expression: {rpn}")
    return stack[0]
            


def main():
    with open(FILENAME) as file:
        lines = [line.strip() for line in file.readlines()]
    
    for line in lines:
        print(f"The result of [{line}] is {rpn_eval(line)}")
    
if __name__ == "__main__":
    main()