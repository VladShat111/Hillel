class Airport:
    seat_place = 150
    baggage_max_weight = 100
    count_of_passengers = 0

    def __init__(self, first_name, second_name, passport_series_number, count_of_baggage, country):
        self.first_name = first_name
        self.second_name = second_name
        self.passport_series_number = passport_series_number
        self.count_of_baggage = count_of_baggage
        self.country = country

        Airport.count_of_passengers += 1


    def online_register(self):
        firstname = input('Enter your first name for online registration')
        secondname = input('Enter your second name for online registration')
        if firstname == self.first_name and secondname == self.second_name:
            print('Your online registration {} has been successful.'.format(self.first_name + ' ' + self.second_name))
        else:
            print('Something wrong, please check your parameters!')



    def check_in(self):
        passport = input('Please, enter your number and series of passport')
        if passport == self.passport_series_number:
            print('Here is your boarding pass. I may go to the passport control')
        else:
            print('Please, check your passport data!')



    def passport_control(self):
        firstname = input("Enter the first name")
        secondname = input("Enter the second name")
        if firstname == self.first_name and secondname == self.second_name:
            print("Everything is good!")
        else:
            print("Please, check your data")

        if self.count_of_baggage <= self.baggage_max_weight:
            print("Your baggage is in order! You may go to the departure of lounge")
        else:
            print("Sorry, you must pay for extra weight!")



    def departure_lounge(self):
        print('Hi {}. You can go to duty free and have relax. After a while you must go to the gate'.format(self.first_name + '' + self.second_name))



    def gate(self):
        passport = input('Please, enter your number and series of passport')
        if passport == self.passport_series_number:
            print('You can go to boarding')
        else:
            print('Please, check your passport data')



    def boarding(self):
        print('Instruction from flight attendants')
        print('Greetings from ship`s commander. And information about the {}.'.format(self.country))







    def board_the_plane(self):
        if self.seat_place >= Airport.count_of_passengers:
            return 'Take of'



Vlad = Airport('Vlad', 'Shatalyuk', 'AB852764', 10, 'England')

Vlad.online_register()
Vlad.check_in()
Vlad.passport_control()
Vlad.departure_lounge()
Vlad.gate()
Vlad.boarding()
Vlad.board_the_plane()

