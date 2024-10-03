def add(a, b):
    return a + b

def sub(a, b):
    return a - b

num1 = int(input())
num2 = int(input())

print(f"덧셈결과 :{ add(num1, num2) }" )
print(f"뺄셈결과 :{ sub(num1, num2) }" )

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide"
    
print(f"곱셈결과 :{ mul(num1, num2) }" )
print(f"나눗셈결과 :{ div(num1, num2) }" )