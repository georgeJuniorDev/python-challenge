purchase_value = float(input("Enter the value of your purchase: "))

if purchase_value >= 100:
    discount = purchase_value * 0.10
    final_value = purchase_value - discount
    
    print(f"You got 10% discount and will pay {final_value}")
else:
    print("Sorry, you didn't get a discount!")