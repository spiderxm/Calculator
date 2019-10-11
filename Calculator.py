op = input('Enter operator either + or - or * or / or ^ : ')[0]
print('Enter 2 numbers:')
num1 = int(input())
num2 = int(input())
if op == '+':
    res = num1 + num2
elif op == '-':
    res = num1 - num2
elif op == '*':
    res = num1 * num2
elif op == '/':
    res = num1 / num2
elif op == '^':
    res = num1 ** num2
print('The result is', res)