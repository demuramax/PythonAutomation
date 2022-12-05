# +, -, *, /

def culc(num1, action, num2):
    actions = ['+', '-', '*', '/']
    if action == '+':
        res = num1 + num2
    elif action == '-':
        res = num1 - num2
    elif action == '*':
        res = num1 * num2
    elif action == '/':
        try:
            res = round(float(num1 / num2),2)
        except ZeroDivisionError:
            res = 0
            print('На ноль делить нельзя!')
    elif action not in actions:
        raise ValueError('Wrong action in function')
    # else:
    #     res = 'Please input the correct math action'
    return res

a = culc(9, '&', 3)
print(a)
