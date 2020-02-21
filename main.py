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

def update_user_balance(user_id, trip_id, balance):
    ub_table = UserBalanceTable(user_id=user_id, trip_id=trip_id, balance=balance)

    ub_table.update_user_balance(balance, user_id, trip_id)
    print("Update user balance done!!!!")
    

def get_all_users():
    user_obj = UserTable()
    return user_obj.get_all_records()
    
def get_all_trips():
    trip_obj = TripTable()
    return trip_obj.get_all_records()

def show_balance(trip_id):
    ub = UserBalanceTable()
    all_users = ub.get_all_trip_users(trip_id)
    for each_bal in all_users:
        print("name===== {} , balance === {}".format(each_bal["name"], each_bal["balance"]))


def balance_sheet(trip_id):
    ub =UserBalanceTable()
    all_users = ub.get_all_trip_users(trip_id)
    final_balance = []
    total_balance =sum([balance["balance"] for balance in all_users])
    each_user_balance = float(total_balance/len(all_users))
    for each_user in all_users:
        ub= each_user["balance"] - each_user_balance
        print("Name:  {},  Balance:  {}".format(each_user["name"], ub))

def expense_manager():
    print(" 1. Add Trip \n2. Add User\n3. Add Expense\n4. Show Balance\n5.Balance Sheet")
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
                print(each_user, trip_id)
                associate_user_with_trip(int(trip_id), each_user)
            expense_manager()


        elif sub_option == 2:
            numer_of_users = input("Enter number of users: ")
            all_user_ids = []
            for i in range(number_of_users):
                all_user_ids.append(add_user())
            for each_user in all_user_ids:
                associate_user_with_trip(each_user, trip_id)
                # Associate to the trip
            expense_manager()
    elif option_selected == 2:
        add_user()
        expense_manager()
    elif option_selected == 3:
        for user in get_all_users():
            print("id ==> {}, name ==> {}".format(user["id"], user["name"]))
        user_selected = int(input("Single User ID: "))
        balance = int(input("ENter amount:"))
        for each_trip in get_all_trips():
            print("id ==> {}, Name==> {}".format(each_trip["id"], each_trip["name"]))
        selected_trip = int(input("Trip ID:  "))
        update_user_balance(user_selected, selected_trip, balance)
        expense_manager()
    elif option_selected == 4:
        for each_trip in get_all_trips():
            print("id==> {}, Name ===> {}".format(each_trip["id"], each_trip["name"]))
        selected_trip = int(input("Select Trip : ")) 
        show_balance(selected_trip)
        expense_manager()
    elif option_selected == 5:
        for each_trip in get_all_trips():
            print("id==> {}, Name ===> {}".format(each_trip["id"], each_trip["name"]))
        selected_trip = int(input("Select Trip : "))
        balance_sheet(selected_trip)
        expense_manager()
    else:
        print("Invalid Action!!!!!!!!")
        expense_manager()


if __name__ == "__main__":
    print("Welcome to Expense Manager Project, to start with select given below options\n\n")
    expense_manager()
