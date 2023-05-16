# below is the Notification class that gets called when a new object of the class is created.
#It takes two arguments, name and number_of_orders, and initializes three instance variables self.name
class Notification:
    def __init__(self,name,number_of_orders):
        self.name = name
        self.number_of_orders = number_of_orders
        self.is_read = False

        #This method changes the value of the is_read instance variable to True to 
        # indicate that the notification has been read.
    def mark_as_read(self):
       self.is_read = True
    # method returns a dictionary that contains name and n.o of orders
    def send_notification(self):
        order_dict={
            "name":self.name,
            "orders":self.number_of_orders
        }
        return order_dict
    # method checks if there are any new orders and if the notification has been read
    def check_notification(self):
        if self.number_of_orders > 0 and not self.is_read:
            print("Hello, you have {} new orders from {}.".format(self.number_of_orders,self.name))
        elif self.is_read:
            print("You have no new notification")
name = "Maria"
number_of_orders = 20
# instantiate a new variable and call the class
new_message = Notification(name,number_of_orders)
notification_dict = new_message.send_notification()
print(notification_dict)
new_message.check_notification()
new_message.mark_as_read()