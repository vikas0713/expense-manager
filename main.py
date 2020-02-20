if __name__ == "__main__":
    from sql import UserTable

    ut = UserTable(name="Vikas", email="vikas0713@gmail.com", ph_no="9805664004")
    ut.insert()
