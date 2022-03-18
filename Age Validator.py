def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (ie a whole number"
                  "with no decimals)")


MINIMUM_AGE = 12
MAXIMUM_AGE = 110
age = number_checker("Please enter the age of the ticket-holder: ")
if age < MINIMUM_AGE:
    print("Sorry, you are to young for this movie")
else:
    while age <= MAXIMUM_AGE:
        age = number_checker("\nPlease enter an integer between 12 and 110: ")

print(f"Age = {age}")
