choice = input('You want to find a person or register yourself ? For find enter "yes" vice versa "no": ')

list_of_customers = {
    'Shatalyuk': ['vladshatalyu@gmail.com', '0963769289'],
    'Kricet': ['kricet@gmail.com', '0692963485'],
    'Gurow': ['gurow@gmail.com', '0732874695']
}


def find_person(value):
    x = list_of_customers.get(value)
    if x:
        print(x)

    else:
        print(value, "not in the list!")


def person_register(key_register, *args,):
    x = list_of_customers.setdefault(key_register, *args)
    if x:
        print("Register was success", x)
        list_of_customers.update()
    else:
        print("Something gos wrong!")

def of_choice(value):
    try:
        if value == 'yes':
            key_to_find = input("Enter name to find: ")
            find_person(key_to_find)
        elif value == 'no':
            key_for_register = input("Enter your name: ")
            value_for_register = input("Enter your email and phone number: ")
            person_register(key_for_register, value_for_register)

        else:
            print("Unknown choice")
    except Exception as e:
        print("Error: ", e)


of_choice(choice)

