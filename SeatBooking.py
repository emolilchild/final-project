class SeatBooking:
    #allow the customer to book a seat
    def __init__(self, seating_plan):
        #initisalise the seating plan again
        self.seating_plan = seating_plan
    def book_seat(self, seat):
        #allow a booking if the seat choosen is available
        if self.seating_plan.check_seat_availability(seat):
            row, col = int(seat[:-1]), seat[-1]
            #book the seat if seat is available
            self.seating_plan.seats[(row, col)] = 'R'
            #tell customer that the seat has been booked successfully
            return f'Seat {seat} booked successfully.'
        else:
            #tell customer that the seat they have choosen is not available
            return 'Seat not available or does not exist.'