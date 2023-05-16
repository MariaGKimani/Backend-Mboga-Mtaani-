class Orders:
    def __init__(self,name,order,payment,deliveryAdress,status) :
        self.order=order
        self.name=name
        self.payment=payment
        self.deliveryAddress=deliveryAdress
        self.status=status
        #create a dictionary of the order attribute and returns it
    def add_order(self):
        orders_dict={
           "name":self.name,
           "order":self.order,
           "payment":self.payment,
           "deliveryAdress":self.deliveryAddress,
           "status":self.status
           
       }
        return orders_dict
    # Prompts the user to input their details
name=input("input your name")
order=input("Input the type of order")
payment=input("Input the type of payment")
deliveryAddress=input("Input your delivery address")
status=input("Add status of your order")
    # An instance of order is assigned to a variable called user
new_Customer=Orders(Name,order,payment,deliveryAddress,status)
user=new_Customer
print(new_Customer.add_order())
