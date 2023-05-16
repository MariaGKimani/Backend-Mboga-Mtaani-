# create a class vendor that will hold the properties of mama_mboga
class Vendor:
    # initialize the vendor with specific attributes
    
    def __init__(self,store_name,store_location,store_description,vendor_id,vendor_name):
        self.store_name = store_name
        self.store_location = store_location
        self.store_description = store_description
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
    #  create a method to create user and use a dictionary to hold the information   
    def create_user(self):
        user_dict={
            "name":self.vendor_name,
            "id":self.vendor_id,
            "store":self.store_name,
            "location":self.store_location,
            "description":self.store_description
             
        }
        return user_dict
# place holder that will provoke the user to input their details
store_name = input("Enter name of the store :")
store_location = input("Enter the store's location :")
store_description = input("Enter a short decription of the store:")
vendor_id = input("Input the vendor's unique Id:")
vendor_name = input("Input the vendor's name:")
#  create an instance of the class Vendor 
  
new_vendor = Vendor(store_name,store_location,store_description,vendor_id,vendor_name)
new_user = Vendor(store_name,store_location,store_description,vendor_id,vendor_name)
print(new_vendor.create_user()) 
                                 # outputs a dictionary with the given values
