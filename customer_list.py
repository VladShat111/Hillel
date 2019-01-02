choice = input('You want to find a person or register yourself ? For find enter "yes" vice versa "no": ')

list_of_customers = {
    'Shatalyuk': ['vladshatalyu@gmail.com', '0963769289'],
    'Kricet': ['kricet@gmail.com', '0692963485'],
    'Gurow': ['gurow@gmail.com', '0732874695']
}


def find_person(value):
    if value in list_of_customers:
        return list_of_customers.items()

    else:
        return False


def person_register(key_for_register, value_for_register):
    x = list_of_customers.setdefault(key_for_register, value_for_register)
    print("", x)


try:
    if choice == 'yes':
        key_to_find = input("Enter name to find: ")
        find_person(key_to_find)
    elif choice == 'no':
        key_for_register = input("Enter your name: ")
        value_for_register = input("Enter your email and phone number: ")
        person_register(key_for_register, value_for_register)

    else:
        print("Unknown choice")
except Exception as e:
    print("Error: ", e)
