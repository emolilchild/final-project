class FreeSeat:
    #allow the customer to cancel their reservation of a seat
    def __init__(self, seating_plan):
        #initialise the seating plan
        self.seating_plan = seating_plan
    def cancel(self, seat):
        #free up a booked seat when customer decides that they want to cancel
        row, col = int(seat[:-1]), seat[-1]
        if self.seating_plan.seats.get((row, col)) == 'R':
            #change the reserved seat to become free and available again
            self.seating_plan.seats[(row, col)] = 'F'
            #return that the action has been completed
            return f'Seat {seat} is now free.'
        else:
            return 'Seat is already free or does not exist.'