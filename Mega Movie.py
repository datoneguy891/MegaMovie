def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank")
        else:
            return response


def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (ie a whole number"
                  "with no decimals)")


# Main Routine
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count < MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left")
    else:
        print(f"\n**** You have ONLY ONE seat left! ****")
    name = input("What's your name? ").title()
    if name != "Xxx":
        count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still"
          f" {MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")

MINIMUM_AGE = 12
MAXIMUM_AGE = 110
age = number_checker("Please enter the age of the ticket-holder: ")
if age < MINIMUM_AGE:
    print("Sorry, you are to young for this movie")
else:
    while age <= MAXIMUM_AGE:
        age = number_checker("\nPlease enter an integer between 12 and 110: ")

print(f"Age = {age}")
