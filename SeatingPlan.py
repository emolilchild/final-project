class SeatingPlan:
    def __init__(self):
        #create a dictionary that contains and represents the layout and seats of the plane
        self.seats = {}
        self.rows = 80
        self.column = ["A", "B", "C", "D", "E", "F"]
        #iterate over the number of rows in the airplane
        for row in range(1, self.rows+1):
            #for each row iterate over each column in the airplane
            for col in self.column:
                #skip over the aisle seats where are not available for booking
                if col != "C" and col != "D":
                    #mark the bookable seats as "F"
                    #the keys of the dictionary will be tuples consisting of rows and columns respectively
                    self.seats[(row, col)] = "F"
    