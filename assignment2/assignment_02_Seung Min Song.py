# Homework 2 for Seung Min Song
# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
# The code will display an empty list  '[]'.
# Can you debug and fix the output? The code should return the entire list
print(numbers[0:5])

# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

def weeklysales():
    sales = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in days:
        sale = int(input(f'What is the store sales for {i}: '))
        sales.append(sale)
    return(sum(sales))

result = weeklysales()
print("Total sales for the week:", result)

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.

travel = [ 'Jamaica', 'Honduras', 'England', 'Ghana', 'The Maldives', ]
print(travel)
print(sorted(travel))
print(sorted(travel, reverse=True))

# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

addressbook = {'Keeno' : 'keen0ag@gmail.com'}

#finds email
def find_email():
    name = input("Enter name: ")
    email = addressbook.get(name)
    if name in addressbook:
        print(f"{name}: {email}")
    else:
        print(f"No email in address book for {name}")

# adds email
def add_name_email():
    name = input("Enter name: ")
    email = input("Enter email: ")
    addressbook[name] = email
    print(f"Email for {name} stored in addressbook as {email} ")
    
#update email
def update_email():
    name = input("Enter name to be updated: ")
    email = addressbook.get(name)

    if email:
        new_email = input("Enter new email: ")
        addressbook[name] = new_email
        print(f"{name}'s email was updated to {new_email}")
    else:
        print(f"No email exists for {name}")

# delete_email
def delete_email():
    name = input("Enter name: ")
    if name in addressbook:
        del addressbook[name]
        print (f"{name} was deleted from addressbook")
    else:
        print(f" No email exists for {name}")

while True:
    print("\n Options: ")
    print("1. Find email")
    print("2. Add namd & email")
    print("3. Update email")
    print("4. Delete email")
    print("5. Close")
    option = int(input("Enter option number: "))

    if option == 1:
        find_email()
    elif option == 2:
        add_name_email()
    elif option == 3:
        update_email()
    elif option == 4:
        delete_email()
    elif option == 5:
        break
    else:
        print("Invalid Reponse")