# shopping_discount_calculator.py

def calculate_discount(total_amount):
    if total_amount >= 5000:
        discount = 0.20
        discount_amount = total_amount * discount
    elif total_amount >= 3000:
        discount = 0.10
        discount_amount = total_amount * discount
    else:
        discount = 0.00
        discount_amount = 0
    
    final_amount = total_amount - discount_amount
    return discount, discount_amount, final_amount

def main():
    try:
        total_purchase = float(input("Enter the total purchase amount: "))
        
        # Calculate the discount and final payable amount
        discount, discount_amount, final_amount = calculate_discount(total_purchase)

        # Display the results
        print("\n--- Discount Details ---")
        print(f"Total Purchase Amount: ₹{total_purchase:.2f}")
        print(f"Discount: {discount * 100}%")
        print(f"Discount Amount: ₹{discount_amount:.2f}")
        print(f"Final Payable Amount: ₹{final_amount:.2f}")
    
    except ValueError:
        print("Error: Please enter a valid numeric amount.")

if __name__ == "__main__":
    main()