from ShowBookingState import ShowBookingState
from SeatBooking import SeatBooking
from SeatAvailability import SeatAvailability
from FreeSeat import FreeSeat
from ExitProgram import ExitProgram
from SeatingPlan import SeatingPlan

def main_menu():
    seating_plan = SeatingPlan()
    seat_availability = SeatAvailability(seating_plan)