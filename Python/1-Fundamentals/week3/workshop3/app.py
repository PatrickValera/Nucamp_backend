from donations_pkg.homepage import show_homepage,donate,show_donations
from donations_pkg.user import login, register


database = {
    "admin": "password123"
}
donations = []
authorized_user = ""

if not authorized_user:
    print("You must be logged in to donate.")
else:
    print(f"Logged in as {authorized_user}")

while True:
    show_homepage()
    option = input("Choose an option: ")
    print("\n")
    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user= register(database,username)
        if not authorized_user: database[username]=password
    elif option == "3":
        if not authorized_user: 
            print("You are not logged in.")
        else:
            donation_string=donate(authorized_user)
            donations.append(donation_string)
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        break
