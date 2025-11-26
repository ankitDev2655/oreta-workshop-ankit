try:
    def sum(a, b):
        return a+b

    a = float(input("Enter a number: "))
    b = float(input("Enter a second number: "))

    result = sum (a,b)
    print(result)  
    
except ValueError:
    print("Invalid input")