# Python program that asks the user to enter a mark (a number between 0 and 100) and then prints the matching letter grade.

try:
    mark = float(input("Enter your mark (0-100): "))

    if 0 <= mark <= 100:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"

        print("Mark:", mark, "->", "Grade:", grade)
# Considering the Edge cases, if the user enters a mark above 100 and below 0
    else:
        print("Invalid Mark. Please enter a value between 0 to 100")   
# Considering the Edge cases, something that is not a number at all and make sure the program does not crash unexpectedly.
except ValueError:
    print("Invalid Input. Please enter a value between 0 to 100")

# Thank You! 
