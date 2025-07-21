
product_info = ("Notebook", 2.5, 4)

product, price, quantity = product_info

# Calculate total cost
total_cost = price * quantity
print(f"Product: {product}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost}")

product_list = list(product_info)
product_list[2] = 10 

# Convert back to tuple
updated_product_info = tuple(product_list)

print("\nUpdated Product Info:")
print(f"Product: {updated_product_info[0]}")
print(f"Price: ${updated_product_info[1]}")
print(f"Quantity: {updated_product_info[2]}")
