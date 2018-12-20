# a boolean-returning function
def is_positive(n):
    if n > 0:
        return True
    else:
        return False

# a shorter version for checking for negative
def is_negative(n):
    return n < 0    # will return a value of True to a negative value
    
def main():
    num1, num2 = get_dimensions() # input two different values into the function
    print(num1, num2)
    
    if is_positive(6):
        print("It is positive.")
    else:
        print("It is not.")
        
    if is_negative(6):
        print("It is negative.")
    else:
        print("It is not.")
        
    if is_positive(num1) and is_positive(num2):
        print("Both of positive")
    else:
        print("Both are not positive.")
    
main()