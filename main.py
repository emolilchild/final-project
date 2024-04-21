from SeatBooking import SeatBooking
from SeatAvailability import SeatAvailability
from FreeSeat import FreeSeat
from ExitProgram import ExitProgram
from SeatBookingState import SeatingPlan

def main_menu():
    #initialise objects from the imported classes and files
    #set up the seating plan instance
    seating_plan = SeatingPlan()
    #setup the instance for the seat availability
    seat_availability = SeatAvailability(seating_plan)
    #setup instance for the booking of seats
    seat_booking = SeatBooking(seating_plan, seat_availability)
    #setup the instance for the cancelation of seats
    free_seat = FreeSeat(seating_plan, seat_booking, seat_booking)
    #set up the termination of the program
    exit_program = ExitProgram()
    #start a loop that will always show the menu after actions are completed
    while True:
        print("--- Apache Airline Seating Menu ---")
        print("1. Check seat availability")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        choice = input("Select an option: ")

        if choice == '1':
            #ask the user to type in the seat they want to check
            seat = input("Enter seat number (e.g., 1A): ")
            #use the seat_availability object to check if the seat is available
            available = seat_availability.check(seat)
            #itell the user if the seat is available or not
            if available:
                print("Seat available!")
            else:
                print("Seat not available.")
        elif choice == '2':
            #ask the user for the seat they want to book
            seat = input("Enter seat number to book (e.g., 1A): ")
            #use the seat_booking object to book the seat
            result = seat_booking.book_seat(seat)
            #print if the action has been completed
            print(result)
        elif choice == '3':
            #ask the user to type in the seat they want to cancel
            booking_reference = input("Enter booking reference to free a seat: ")
            #use the free_seat object to free up the seat
            result = free_seat.cancel(booking_reference)
            #print if the action has been completed
            print(result)
        elif choice == '4':
            #show the seating plane and layout of the plane
            seating_plan.display()
        elif choice == '5':
            #use the exit_program object to end the program
            if exit_program.exit_program() == 'exit':
                #if the exit_program method returns 'exit', break out of the loop to end the program.
                break
        else:
            #invalid input given by the user
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()