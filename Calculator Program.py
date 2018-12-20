# get two numbers and do arthemtic on them

# menu function
def menu():
    print("Q : Quit")
    print("+ : Addition")
    print("/ : Division")
    print("- : Subtraction")
    print("* : Multiplication")
    
# read and return a selection from the user
# "value-returning function"
def get_choice():
    ch = input("Enter your choice [Q+/-*]: ")
    return ch

# read a number from a user and convert to a number and return
def get_num(s):
    print("Enter your", s, "number: ", end="")
    n = float(input())
    return n

def do_add(a, b):
    c = a + b
    return c

def do_mul(a, b):
    c = a * b
    return c

def do_div(a, b):
    c = a / b # c is a local variable
    return c

def do_sub(a, b):
    c = a - b
    return c

def display (a):
    print(format(a,".3f"))

# main function is where all the logic is
def main():
    # use pass as a placeholder
    
    choice =""
    while choice != "Q":
        menu()
        choice = get_choice()
        num1 = get_num("first")
        num2 = get_num("second")
        
        answer = "undefined"
        # decision structure
        if choice == "+":
            answer = do_add(num1, num2)
        elif choice == "/":
            answer = do_div(num1, num2)
        elif choice == "-":
            answer = do_sub(num1, num2)
        elif choice == "*":
            answer = do_mul(num1, num2)
        elif choice == "Q":
            print("Goodbye")
        else:
            print("Invalid selection!")
        
        if answer != "undefined":
            display(answer)
        else:
            print(answer)
    
main()