# discount_calculator.py
# Week Three Assignment: Function to calculate discount

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.

    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage (0 to 100)

    Returns:
    float: Final price after discount or original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Output result
    if discount_percentage >= 20:
        print(f"A discount of {discount_percentage}% was applied.")
        print(f"Final price: KSH{final_price:.2f}")
    else:
        print(f"No discount was applied (less than 20%).")
        print(f"Original price: KSH{original_price:.2f}")

except ValueError:
    print("Please enter a valid number for price and discount.")
