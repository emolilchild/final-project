from SeatBooking import SeatBooking
from SeatAvailability import SeatAvailability
from FreeSeat import FreeSeat
from ExitProgram import ExitProgram
from SeatBookingState import SeatingPlan

def main_menu():
    seating_plan = SeatingPlan()
    seat_availability = SeatAvailability(seating_plan)
    seat_booking = SeatBooking(seating_plan)
    free_seat = FreeSeat(seating_plan)