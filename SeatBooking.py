class SeatBooking:
    #allow the customer to book a seat
    def __init__(self, seating_plan, seat_availability):
        #initisalise the seating plan again
        self.seating_plan = seating_plan
        #initialise the seat availability instance to check if seat is available
        self.seat_availability = seat_availability
    def book_seat(self, seat):
        #allow a booking if the seat choosen is available
        #since seat is expected to be in a string
        #check if seat is available
        if self.seat_availability.check(seat):
            #if available split the string into row and column separately
            row, col = int(seat[:-1]), seat[-1]
            #book the seat if seat is available and mark it "R"
            self.seating_plan.seats[(row, col)] = 'R'
            #tell customer that the seat has been booked successfully
            return f'Seat {seat} booked successfully.'
        else:
            #tell customer that the seat they have choosen is not available
            return 'Seat not available or does not exist.'