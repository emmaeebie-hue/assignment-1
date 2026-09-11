from product_data import products
print(products[0])
print(products[1])
print(products[2])
# TODO: Step 1 - Print out the products to see the data that you are working with.



# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference) 

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    product["tags"] = set(product["tags"])
    converted_products.append(product)




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    matches = product_tags.intersection(customer_tags)
    return len(matches)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        recommendations.append((product["name"], match_count))

    return sorted(recommendations, key=lambda x: x[1], reverse=True)



# TODO: Step 7 - Call your function and print the results

recommendations = recommend_products(converted_products, customer_preferences)
print(recommendations)



# DESIGN MEMO (write below in a comment):
# 1. I used loops to go through the products and process their tags.
#    I also used set intersection to find tags that matched the customer's
#    preferences. Sets were useful because they remove duplicates and make
#    comparisons easier.
# 2. If there were 1000+ products, I would still use sets to make the
#    comparisons efficient. I could also organize or index the product tags
#    so the program would not have to check every product each time.

