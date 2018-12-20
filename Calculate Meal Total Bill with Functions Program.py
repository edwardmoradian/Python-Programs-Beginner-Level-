# Author:  Edward Moradian


def get_cost():
    cost = float(input("Please enter the cost of your meal: $ "))
    while cost < 0.00:
        print("\nPlease enter a valid cost.", end="")
        cost = float(input("Please enter the cost of your meal: $ "))
    return cost

def compute_tip(cost):
    tiprate = .18
    tip = cost * tiprate
    return tip

def compute_tax(cost):
    taxrate = .0825
    tax = cost * taxrate
    return tax

def compute_grand_total(cost,tip,tax):
    grand_total = cost + tip + tax
    return grand_total

def display_total_cost(cost,tip,tax,grand_total):
    print("\nCost:\t $",format(cost,".2f"))
    print("Tip:\t $",format(tip,".2f"))
    print("Tax:\t $",format(tax,".2f"))
    print("Total:\t $",format(grand_total,".2f"))

def main():
    cost = get_cost()
    tip = compute_tip(cost)
    tax = compute_tax(cost)
    grand_total = compute_grand_total(cost,tip,tax)
    display_total_cost(cost,tip,tax,grand_total)
    
main()