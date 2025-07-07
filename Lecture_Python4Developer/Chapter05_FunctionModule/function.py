def func():
    print("This is a Function. Hello!")
func()

def func(name):
    print(f"This is a Function. Hello! {name}")
func("Park")

def sum(num1, num2):
    return num1 + num2
print(f"Result: {sum(10, 20)}")

def div(num1, num2):
    if (num2 == 0):
        return 0
    return num1 / num2
result_div = div(3,2)
print(f"divide result = {result_div}")