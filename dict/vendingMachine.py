products = {             # products dictionary
    "soda": 90,
    "chips": 60,
    "candy": 50,    
    "chocolate": 110,
    "gum": 90
}

def display_products():
    print("Products:")
    for product, price in products.items():
        print(f"{product}: {price}Rsd")

def calculate_total(selected_products):
    total = 0
    for product in selected_products:
        total += products[product]
    return total

def main():
    print("Welcome to the vending machine!")
    display_products()

    selected_products = {}
    while True:
        choice = input("Enter the product you fancied: ")
        if choice == "done":
            break
        if choice in products:
            quantity = int(input("Enter the quantity: "))
            selected_products[choice] = products[choice] * quantity
            print(f"{quantity} {choice} added to cart")
        else:
            print("This product is currently unavailable")
    if len(selected_products) > 0:
        print("\nSelected products:")
        for name, total in selected_products.items():
            print(f"{name}: {total}Rsd")

if __name__ == "__main__":
    main()