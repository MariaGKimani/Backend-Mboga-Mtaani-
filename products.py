class Products:

    #method to initalize attributes
    def __init__(self, name, description, price, quantity, image):
        self.product_name = name
        self.product_description = description
        self.product_price = price
        self.product_quantity = quantity
        self.product_image = image
    
    #method to add products to the products list in the web app
    def add_product(self):
        product_dict = {                #dictionary to represent attributes and their values 
            "name": self.product_name,
            "description": self.product_description,
            "price": self.product_price,
            "quantity": self.product_quantity,
            "image": self.product_image
        }
        
        return product_dict

products_list = []      #empty list to store all products

num_products = int(input("How many products do you want to add? "))      #prompt to enter no of produts to be added

#loop to iterate over number of products to be added, and prompt user to enter details of each product
for i in range(num_products):
    name = input(f"Enter the name of product {i+1}: ")
    description = input(f"Enter the description of product {i+1}: ")
    price = float(input(f"Enter the price of product {i+1}: "))
    quantity = int(input(f"Enter the quantity of product {i+1}: "))
    image_url = input(f"Enter the URL of product {i+1} image: ")
    
    product = Products(name, description, price, quantity, image_url)    #object instantiation
    products_list.append(product)       #adding new products to the all products list
    
    product_dict = product.add_product()     #obtaining new products in dictionary structure
    print(product_dict)


#method to edit existing products, takes wholeproduct list as a parameter
def edit_products(products_list):
    edit_product = input("Which product do you want to edit?:")      #prompt to enter product to be edited

    #looping through list of all products 
    for product in products_list: 
        if product.product_name == edit_product:       #checking if the input product is in the list, if found, prompts to enter new details
            new_name = input("Enter the new name: ")
            new_description = input("Enter the new description: ")
            new_price = float(input("Enter the new price: "))
            new_quantity = int(input("Enter the new quantity: "))
            new_image_url = input("Enter the new image URL: ")
            
            #updating the product to match new values
            product.product_name = new_name
            product.product_description = new_description
            product.product_price = new_price
            product.product_quantity = new_quantity
            product.product_image = new_image_url
            
            return "Product edited successfully."
        
        else:
            print("Product not found.")

edit_products(products_list)

#method to delete products from the product list, takes whole product list as a parameter
def delete_product(products_list):
    delete_product = input("Which product do you want to delete? ")

    #iterating through product list
    for product in products_list:
        if product.product_name == delete_product:     #checking if the input product is in the list, if found, it is removed
            products_list.remove(product)
            return "Product deleted successfully."
        
        else:
            print("Product not found.")
            
delete_product(products_list)