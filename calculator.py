def calculator(op, num1, num2):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    elif op == 5:
        return num1 ** num2


op = int(input(f'Welche Operation willst du durchführen?\n1. Addition\n2. Substration\n3. Multiplikation\n4. Division\n5. Exponent\nNR: '))
num1 = int(input('Erste Zahl: '))
num2 = int(input('Zweite Zahl: '))

print(calculator(op, num1, num2))
