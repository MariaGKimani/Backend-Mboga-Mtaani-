class User:#initialising the init class with the init method
    def __init__(self, name, email, password, phone_number, address):
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address
#the dict holds the user information
    def get_user(self):#returns the dictionary containing the user information
        user_dict= {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "address": self.address,
        }
        return user_dict

    def login(self, email, password):#checks if the email and password mathches the user information
        if self.email == email and self.password == password:
            print("Login successful")
        else:
            print("Wrong password and email,please try again")

#prompts the user to enter their details
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
phone_number = input("Enter your phone number: ")
address = input("Enter your address: ")
     
new_user = User(name,email,password,phone_number,address)
user_dict = new_user.get_user()
print(user_dict)

login_email = input("Enter your email to login: ")
login_password = input("Enter your password to login: ")
new_user.login(login_email, login_password)