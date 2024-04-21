import random
class SeatBooking:
    #allow the customer to book a seat
    def __init__(self, seating_plan, seat_availability):
        #initisalise the seating plan again
        self.seating_plan = seating_plan
        #initialise the seat availability instance to check if seat is available
        self.seat_availability = seat_availability
        #for part b intialise the customer data
        self.customer_data = {}

    #part B of the project
    #add a new set to keep track of booking references
    booking_references = set()

    def generate_unique_booking_reference(self):
        uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        possible_characters = uppercase_chars + digits
        while True:
            #create a list of random choices.
            random_characters = random.choices(possible_characters, k=8)

            #join the list into a string to form the reference.
            reference = ''.join(random_characters)

            #if the reference is unique, return it if not a new reference will be generated again
            if reference not in self.booking_references:
                self.booking_references.add(reference)
                return reference
    #for part b customer_data will also be a parameter
    def book_seat(self, seat, customer_data):
        #for part b i have added this next line of code
        #assume that customer_data is in a dictionary
        reference = self.generate_unique_booking_reference()
        #allow a booking if the seat choosen is available
        #since seat is expected to be in a string
        #check if seat is available
        if self.seat_availability.check(seat):
            #if available split the string into row and column separately
            row, col = int(seat[:-1]), seat[-1]
            #book the seat if seat is available and mark it "R"
            #for part B i have refractored the code so that "R" becomes the booking reference
            self.seating_plan.seats[(row, col)] = reference
            #store the customer data in a dictionary
            self.customer_data[reference] = customer_data
            #tell customer that the seat has been booked successfully
            #have refactor the code for part b so that it will also return booking reference
            return f'Seat {seat} booked successfully. Here is your booking reference {reference}'
        else:
            #tell customer that the seat they have choosen is not available
            return 'Seat not available or does not exist.'


