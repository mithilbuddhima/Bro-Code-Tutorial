foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")

total = sum(prices)
print(f"Total: ${total:.2f}")