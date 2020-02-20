from sql import UserTable, TripTable


def add_trip():
    trip_name = input("Enter Trip Name : ")
    trip_obj = TripTable(name=trip_name)
    trip_obj.insert()

def add_user():
    name = input("Enter full name: ")
    email = input("Enter Email :")
    ph_no = input("Enter phone number: ")
    user_obj = UserTable(name=name, email=email, ph_no=ph_no)
    user_obj.insert()
    
def expense_manager():
    print(" 1. Add Trip \n 2. Add User\n")
    option_selected = int(input("Enter option :"))
    print(option_selected) 
    if option_selected == 1:
        add_trip()
    elif option_selected == 2:
        add_user()
    else:
        print("Invalid Action!!!!!!!!")


if __name__ == "__main__":
    print("Welcome to Expense Manager Project, to start with select given below options\n\n")
    expense_manager()
