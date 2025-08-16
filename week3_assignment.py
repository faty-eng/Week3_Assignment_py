def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount 
    percentage is 20% or higher. Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Main Program ---
try:
    # Prompt user for input
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call function
    final_price = calculate_discount(price, discount_percent)

    # Display result
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")