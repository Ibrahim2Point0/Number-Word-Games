KnowsPalindrome = input("Do you know what a palindrome is? Enter: 'Y' or 'N': ")


if KnowsPalindrome == "N":
    print("A palindrome is a word, number, phrase, or other sequence of "
          "symbols that reads the same backwards as forwards. For example: "
          "'madam', read backwards is 'madam'.")

PlayGame = input("Do you want to play the Palindrome Game? Enter: 'Y' or 'N': ")

while PlayGame == "Y":
    if PlayGame == "Y":
        character_sequence = input("Enter a word and I will tell you if it is a "
                               "palindrome: ")

        character_sequence_reversed = character_sequence[::-1]

        if character_sequence == character_sequence_reversed:
            print(f"'{character_sequence}' is a palindrome!")
        else:
            print(f"'{character_sequence}' is not a palindrome. '"
              f"{character_sequence}' does not read the same forward and "
              f"backward.")
    PlayGame = input("Do you want to enter another word? 'Y' or 'N': ")

else:
    print("Okay, maybe next time. Have a nice day!")