def display_title():
    print("Welcome to the Grade Calculator")


def get_total_points():
    while True:
        try:
            total_points = int(input("Enter the total score (0-1000): "))
            if 0 <= total_points <= 1000:
                return total_points
            else:
                print("You must enter integer values between 0 and 1000. Try again.")
        except ValueError:
            print("Please enter a valid integer.")


def get_letter_grade(average_earned):
    if 92 <= average_earned <= 100:
        return 'A'
    elif 88 <= average_earned <= 91.99:
        return 'B+'
    elif 82 <= average_earned <= 87.99:
        return 'B'
    elif 78 <= average_earned <= 81.99:
        return 'C+'
    elif 70 <= average_earned <= 77.99:
        return 'C'
    elif 60 <= average_earned <= 69.99:
        return 'D'
    else:
        return 'F'


def main():
    display_title()
    choice = 'y'
    while choice.lower() == 'y':
        total_points = get_total_points()
        average = total_points / 10
        letter_grade = get_letter_grade(average)
        print(f"You earned an average of: {average:.1f}%.")
        print("Letter grade earned:", letter_grade)
        choice = input("Would you like to enter another score (y/n)? ")


if __name__ == "__main__":
    main()
