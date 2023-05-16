class CheckOrders:
    def __init__(self,customer_name):
        self.orders = []
        self.customerName=customer_name
#  adds the new orders to the orders list
    def add_order(self, order):
        self.orders.append(order)
# removes an order to the list
    def remove_order(self, order):
        self.orders.remove(order)
# you can get orders from the list
    def get_orders(self):
        return self.orders
    def get_order_by_id(self, name):
        for order in self.orders:
            if name == name:
                return order
# used to represent a single order
class Orders:
    def __init__(self,name,order,payment,deliveryAdress,status) :
        self.order=order
        self.name=name
        self.payment=payment
        self.deliveryAddress=deliveryAdress
        self.status=status
        #  returns a dictionary containing the details
    def add_order(self):
        orders_dict={
           "name":self.name,
           "order":self.order,
           "payment":self.payment,
           "deliveryAdress":self.deliveryAddress,
           "status":self.status
       }
        return orders_dict
name=input("input your name")
order=input("Input the type of order")
payment=input("Input the type of payment")
deliveryAddress=input("Input your delivery address")
status=input("Add status of your order")
new_Customer=Orders(name,order,payment,deliveryAddress,status)
user=new_Customer
print(new_Customer.add_order())
my_orders = CheckOrders("John Doe")
new_order = Orders("Jill", "Product A", 10.99,"JNFJ","LDJNF")
print(my_orders.add_order(new_order))
all_orders = my_orders.get_orders()
# all orders are retrieved using the get_order_id method
name = "Jill"
order = my_orders.get_order_by_id(name)
