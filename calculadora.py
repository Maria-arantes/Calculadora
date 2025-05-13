def calcular(num1, num2, operacao):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except (ValueError, TypeError):
        return None

    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return None
        return num1 / num2
    elif operacao == '^':
        return num1 ** num2
    else:
        return None
