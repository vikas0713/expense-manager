from sql import UserTable, TripTable, UserBalanceTable


def add_trip():
    trip_name = input("Enter Trip Name : ")
    trip_obj = TripTable(name=trip_name)
    return trip_obj.insert()

def add_user():
    name = input("Enter full name: ")
    email = input("Enter Email :")
    ph_no = input("Enter phone number: ")
    user_obj = UserTable(name=name, email=email, ph_no=ph_no)
    return user_obj.insert()

def associate_user_with_trip(trip_id, user_id, balance=0):
    ub_table = UserBalanceTable(user_id=user_id, trip_id=trip_id, balance=0)
    ub_table.insert()
    print("User balance table updated")
    

def get_all_users():
    user_obj = UserTable()
    return user_obj.get_all_records()
    
def expense_manager():
    print(" 1. Add Trip \n 2. Add User\n")
    option_selected = int(input("Enter option :"))
    print(option_selected) 
    if option_selected == 1:
        trip_id= add_trip()
        print("1. Add existing users \n 2. Add new User")
        sub_option = int(input("Your option:  "))
        if sub_option == 1:
            all_existing_users = get_all_users()
            for user in all_existing_users:
                print("id: {},   name: {}".format(user["id"], user["name"]))
            selected_users = input("Enter User id's")
            selected_users = [int(x) for x in selected_users.split(",")]
            print("Updating records.................")
            for each_user in selected_users:
                associate_user_with_trip(each_user, trip_id)
            expense_manager()


        elif sub_option == 2:
            numer_of_users = input("Enter number of users: ")
            for i in range(number_of_users):
                add_trip()
                # Associate to the trip
    elif option_selected == 2:
        add_user()
    else:
        print("Invalid Action!!!!!!!!")


if __name__ == "__main__":
    print("Welcome to Expense Manager Project, to start with select given below options\n\n")
    expense_manager()
