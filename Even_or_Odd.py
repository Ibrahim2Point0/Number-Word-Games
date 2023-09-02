# This game will help the user identify if a number is EVEN or ODD. The program will ask the user to input a whole number and the program will tell the user if the inputed number is EVEN or ODD.

start_game = input("Do you want to play the 'Is it Even or Odd' game? Enter 'Y' or 'N': ")

while start_game == "Y":
    if start_game == "Y":
        user_number = int(input("Enter a whole number and I will tell you if the number is 'EVEN' or 'ODD'. For example '2' or '15'. Number: "))
        if user_number % 2 == 0:
            print(f"{user_number} is EVEN.")
        else:
            print(f"{user_number} is ODD.")
    start_game = input("Do you want to enter another number? Enter 'Y' or 'N': ")


else:
    print("Okay. Have a nice day!")