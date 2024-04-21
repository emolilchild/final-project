class SeatingPlan:
    def __init__(self):
        #create a dictionary that contains and represents the layout and seats of the plane
        self.seats = {}
        #define the number of rows there are in the plane layout
        self.rows = 80
        #define the columns in each row where "X" will represent the aisle between row C and D
        self.column = ["A", "B", "C", "X", "D", "E", "F"]
        #iterate over the number of rows in the airplane
        for row in range(1, self.rows+1):
            #for each row iterate over each column in the airplane
            for col in self.column:
                #mark the bookable seats as "F"
                #the keys of the dictionary will be tuples consisting of rows and columns respectively
                self.seats[(row, col)] = "F"
            #mark the aisle with "X"
            for row in range(1, self.rows+1):
                self.seats[(row, "X")] = "X"
            #mark the storage spaces with "S"
            for col in ["D", "E", "F"]:
                #only space 77DEF and 78DEF are storage areas
                self.seats[(77, col)] = "S"
                self.seats[(78, col)] = "S"
    def display(self):
        #tell the user the status of the seat selected
        #iterate through the columns to get the status of each seat
        for row in range(1, self.rows +1):
            row_display = f"Row {row}"
            for col in self.column:
                #get the seat status from the dictionary
                seat_status = self.seats.get((row, col), "")
                row_display += f"{seat_status}"
            print(row_display)
