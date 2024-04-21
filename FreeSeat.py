class FreeSeat:
    #allow the customer to cancel their reservation of a seat
    #for part b initialise customer data and booking reference
    def __init__(self, seating_plan, customer_data, booking_reference):
        #initialise the seating plan
        self.seating_plan = seating_plan
        #part b
        self.customer_data = customer_data
        self.booking_reference = booking_reference
    #for part b refactor seat into booking_reference for the parameter
    def cancel(self, booking_reference):
        #free up a booked seat when customer decides that they want to cancel
        #code in comment for the next few lines is my part A
        #row, col = int(seat[:-1]), seat[-1]
        #if self.seating_plan.seats.get((row, col)) == 'R':
            #change the reserved seat to become free and available again
            #self.seating_plan.seats[(row, col)] = 'F'
        #part b of the project
        #check if the provided booking reference is valid
        if booking_reference in self.booking_reference:
            #find the seat that matches the booking reference
            seat_to_free = None
            #iterate over each seat in the seating plan
            for seat in self.seating_plan.seats:
                #get reference associated with the current seat
                ref = self.seating_plan.seats[seat]
                #check if current seat matches the booking reference
                if ref == booking_reference:
                    #free the seat
                    seat_to_free = seat
                    #exit the loop
                    break
            #if seat would with booking reference
            if seat_to_free:
                #mark the seat as free "F"
                self.seating_plan.seats[seat_to_free] = "F"
                #check if the booking reference in the data
                if booking_reference in self.customer_data:
                    #remove customer data
                    del self.customer_data[booking_reference]
                #remove the booking reference
                self.booking_reference.discard(booking_reference)
                # return that the action has been completed
                return f"Booking with reference {booking_reference} has been canceled"
            else:
                return "No seat found with the given booking reference"
        else:
            return 'Seat is already free or does not exist.'