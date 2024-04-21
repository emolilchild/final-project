class SeatAvailability:
    #initialise the seating plan
    def __init__(self, seating_plan):
        self.seating_plan = seating_plan
    def check(self, seat):
        #check if a seat is available
        #get the row using slicing of a string
        row = int(seat[:-1])
        #get column using negative indexing
        col = seat[-1]
        #get the status of the seat
        #value will be returned only if the key exist
        seat_status = self.seating_plan.seats.get((row, col))
        #return if the status of the seat is free or not
        if seat_status == "F":
            return True
        else:
            return False
