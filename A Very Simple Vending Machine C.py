
"""
VENDING MACHINE - All Requirements Met (AED Currency)
"""

items = {
    "A1": ["Cola", 10.00, 5, "Drink"],
    "A2": ["Water", 6.00, 8, "Drink"],
    "A3": ["Coffee", 12.00, 4, "Hot"],
    "B1": ["Chips", 8.00, 6, "Snack"],
    "B2": ["Chocolate", 10.00, 3, "Snack"],
    "B3": ["Biscuits", 7.00, 2, "Snack"]
}

suggest = {"A3": "B3", "B2": "A1"}  # Coffee->Biscuits, Chocolate->Cola
money = 0  # AED collected
sold = []  # Items sold

def menu():
    print("\n=== VENDING MACHINE MENU ===")
    print("All prices in AED")
    for code, (name, price, stock, type) in items.items():
        stock_msg = " [OUT]" if stock == 0 else f" [{stock} left]"
        print(f"{code}: {name:12} AED {price:5.2f}{stock_msg}")

def buy():
    global money
    menu()
    
    while True:
        code = input("\nEnter code (or 'X' to stop): ").upper()
        if code == "X": 
            break
        
        if code in items and items[code][2] > 0:
            name, price, stock, type = items[code]
            
            # Get AED
            while True:
                try: 
                    m = float(input(f"{name} costs AED {price}. Insert AED: "))
                except: 
                    continue
                if m > 0: 
                    break
            
            # Check money
            if m < price:
                print(f"Need AED {price-m} more.")
                continue
            
            # Process
            change = m - price
            items[code][2] -= 1
            money += price
            sold.append(code)
            
            print(f"Dispensing {name}...")
            if change > 0: 
                print(f"Change: AED {change}")
            
            # Suggest
            if code in suggest:
                sug = suggest[code]
                if items[sug][2] > 0:
                    yn = input(f"Add {items[sug][0]} for AED {items[sug][1]}? (y/n): ")
                    if yn == 'y':
                        items[sug][2] -= 1
                        money += items[sug][1]
                        sold.append(sug)
                        print(f"Added {items[sug][0]}!")
            
            # More?
            if input("\nAnother item? (y/n): ") != 'y': 
                break
        else:
            print("Invalid or out of stock.")

# Run
print("VENDING MACHINE (AED)")
while True:
    buy()
    if input("\nNext customer? (y/n): ") != 'y': 
        break

# Stats
print(f"\nTotal collected: AED {money:.2f}")
print(f"Items sold: {len(sold)}")
for code in items:
    if items[code][2] <= 2:
        print(f"Low stock: {items[code][0]} ({items[code][2]} left)")