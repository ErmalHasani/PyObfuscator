def __obf_0001__(name):
    return f'Hello, {name}!'

def __obf_0002__(a, b):
    result = a + b
    return result

def __obf_0003__():
    name = __builtins__.__import__("base64").b64decode(b"QWxpY2U=").decode()
    number1 = 10
    number2 = 20
    print(__obf_0001__(name))
    print(f'The sum of {number1} and {number2} is {__obf_0002__(number1, number2)}')
if __name__ == __builtins__.__import__("base64").b64decode(b"X19tYWluX18=").decode():
    __obf_0003__()