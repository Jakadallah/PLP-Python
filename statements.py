def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Example usage:
original_price = 2000
discount_percentage = 15
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)
 #asignment 2
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

def main():
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    if final_price == original_price:
        print("No discount applied. Final price:", final_price)
    else:
        print("Final price after applying discount:", final_price)

if __name__ == "__main__":
    main()