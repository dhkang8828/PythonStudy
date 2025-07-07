'''
    Function
    
'''
def sum(num1, num2):
    print(f"first value: {num1}")
    print(f"second value: {num2}")
    return num1 + num2

def inputInteger():
    while (True):
        try:
            value = int(input("input value: "))
        except ValueError:
            print(f"ValueError has Occured. Please enter again")
            continue
        else:
            return value

val1 = inputInteger()
print(f"val1: {val1}")


        
    