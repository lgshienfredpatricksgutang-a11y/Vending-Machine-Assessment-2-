
"""
VENDING MACHINE - All Requirements Met (AED Currency)
"""

items = {                                                                   # Item lists with code: [name, price, stock, type]
    "A1": ["Cola", 10.00, 5, "Drink"],
    "A2": ["Water", 6.00, 8, "Drink"],
    "A3": ["Coffee", 12.00, 4, "Hot"],
    "B1": ["Chips", 8.00, 6, "Snack"],
    "B2": ["Chocolate", 10.00, 3, "Snack"],
    "B3": ["Biscuits", 7.00, 2, "Snack"]
}

suggest = {"A3": "B3", "B2": "A1"}  # Coffee->Biscuits, Chocolate->Cola      # suggest items to buy together 
money = 0                                                                    # AED collected
sold = []                                                                    # how many items sold

def menu():                                                                  # Displays the vending machine menu with item codes, names, prices, and stock status.
    print("\n=== VENDING MACHINE MENU ===")
    print("All prices in AED")
    for code, (name, price, stock, type) in items.items():
        stock_msg = " [OUT]" if stock == 0 else f" [{stock} left]"
        print(f"{code}: {name:12} AED {price:5.2f}{stock_msg}")

def buy():
    global money                                                               # Function to handle the buying process
    menu()
    
    while True:                                                                   # Main loop for purchasing items from the vending machine.
        code = input("\nEnter code (or 'X' to stop): ").upper()
        if code == "X": 
            break
        
        if code in items and items[code][2] > 0:                                  # Checks if the entered code is valid and if the item is in stock.
            name, price, stock, type = items[code]
            
            
            while True:                                                                       # Gets the AED amount from the user to pay for the selected item.
                try: 
                    m = float(input(f"{name} costs AED {price}. Insert AED: "))
                except: 
                    continue
                if m > 0: 
                    break
            
            
            if m < price:                                                                      # This code here checks if the inserted money is less than the price of the item.
                print(f"Need AED {price-m} more.")
                continue
            
            
            change = m - price                                                                # This process calculates the change to be returned to the customer.
            items[code][2] -= 1
            money += price
            sold.append(code)
            
            print(f"Dispensing {name}...")                                                    # this line of code dispenses the selected item to the customer.
            if change > 0: 
                print(f"Change: AED {change}")
            
            
            if code in suggest:                                                               # Suggest an item if applicable
                sug = suggest[code]                                                           # The code here gets the suggested item code based on the purchased item code.
                if items[sug][2] > 0:                                                         # If suggested item has stock
                    yn = input(f"Add {items[sug][0]} for AED {items[sug][1]}? (y/n): ")       # Ask: "Add [item] for AED [price]? (y/n)"
                    if yn == 'y':                                                             # If yes
                        items[sug][2] -= 1                                                    # Add it to purchase (update stock, money, sold)
                        money += items[sug][1]
                        sold.append(sug)
                        print(f"Added {items[sug][0]}!")
            
           
            if input("\nAnother item? (y/n): ") != 'y':                     # Ask if the customer wants to buy another item. if not, exit the loop.
                break
        else:
            print("Invalid or out of stock.")                                 # Invalid code or out of stock message.


print("VENDING MACHINE (AED)")                                              # Welcome message to the vending machine when it starts.
while True:
    buy()                                                                     # One customer's shopping session
    if input("\nNext customer? (y/n): ") != 'y':                              # Ask: "Next customer? (y/n)"
        break                                                                 # Exit the main loop if there are no more customers. # Stop if no more customers


print(f"\nTotal collected: AED {money:.2f}")                                  # The Summary of the total money collected by the vending machine and the number of items sold.
print(f"Items sold: {len(sold)}")
for code in items:                                                            
    if items[code][2] <= 2:                                                   # Low stock warning for items with 2 or fewer left in stock.

        print(f"Low stock: {items[code][0]} ({items[code][2]} left)")         # Warning for low stock items # Show low stock warnings (items with 2 or less left)
