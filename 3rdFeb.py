"""
Question: Movie Theatre Booking System
Problem: Build a booking system for a 350-seat theatre that validates age restrictions (12+ only) and seat availability.

Rules:

Theatre capacity: 350 seats (fixed)
Each booking: 1-15 tickets only
Age restriction: 12 years or above
Stop when: Theatre full OR user enters 0
Input: Repeatedly ask for the number of tickets (0 to exit), then the age of each person for valid bookings.

Output: Print booking status for each attempt, then final report showing total bookings, tickets sold, rejected bookings, and remaining seats.

Sample:

Input: 5, then ages: 15, 14, 13, 12, 11 → Output: BOOKING REJECTED - Age restriction

Input: 3, then ages: 20, 18, 16 → Output: BOOKING CONFIRMED - 3 tickets

Input: 0 → Final Report: Total Bookings: 1, Total Tickets Sold: 3, Rejected Bookings: 1, Remaining Seats: 347

Requirements: Use a while loop (main booking), continue statement (skip invalid tickets), for loop (check ages), and break statements (exit loops when needed).
"""

capacity=350
total_tickets_sold=0
total_bookings=0
rejected_bookings=0

print("=============|Python's Movie Theatre Booking System|=============")

while total_tickets_sold<capacity:
    #asking for no.of tickets:
    no_of_tickets_needed=input(f"\nEnter number of tickets:(Remaining={capacity-total_tickets_sold}, 0 to exit):")
    num_tickets=int(no_of_tickets_needed)

    #exit condition to break the program if the user enters "0"
    if num_tickets==0:
        break
    #checking ticket range and availability
    if num_tickets<1 or num_tickets>15:
        print("BOOKING REJECTED - Each booking must be between 1 and 15 only.")
        rejected_bookings+=1
        continue
    #age validation
    all_ages_valid=True
    print(f"Enter the age for each of the {num_tickets} people:\n")
    for i in range(num_tickets):
        age=int(input(f"Age of person {i+1}:"))
        if age<12:
            all_ages_valid=False
            break
    #booking status:
    if all_ages_valid:
        total_tickets_sold+=num_tickets
        total_bookings+=1
        print(f"BOOKING CONFIRMED:- {num_tickets} tickets.\n")
    else:
        rejected_bookings+=1
        print("BOOKING REJECTED:- Age requirement not met [12+ only].\n")
    
#Finalising the booking, rejections, etc
print("================================")
print("Finalised Status:")
print(f"Total Bookings:{total_bookings}")
print(f"Total Tickets Sold:{total_tickets_sold}")
print(f"Rejected Bookings:{rejected_bookings}")
print(f"Remaining Seats:{capacity-total_tickets_sold}")
print("================================")