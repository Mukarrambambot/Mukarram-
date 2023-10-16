def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Input from the user for the target product
target = input("Enter the target product name: ")

# Example product list
products = ["apple", "banana", "apple", "orange", "apple"]

result = linear_search_product(products, target)

if result:
    print(f"The target product '{target}' was found at indices: {result}")
else:
    print(f"The target product '{target}' was not found in the list.")
