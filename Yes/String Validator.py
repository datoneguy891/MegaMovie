def get_snacks():
    snack_choice_error = "Sorry, that is not a valid choice"
    valid_snacks = [["Popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"], ["pita chips", "chips", "pc", "pita",
                    "c", "3"], ["water", "w", "4"]]
    snack_choice = input("Snack: ").lower()
    for snack in valid_snacks:
        if snack_choice in snack:
            snack_choice = snack[0].title()
            return snack_choice

    print(snack_choice_error)
    return get_snacks()


for test in range(6):
    print(f"You want {get_snacks()}")
