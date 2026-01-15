import random

print("\L WELCOME")

print("\n\tPASSWARD GENERATOR")

characters =["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s","d", "f", "g", "h", "j", "k", "1","2", "x", "o", "v", "b", "n","m", "Q", "E", "R","T","Y" ,"U", "I", "O", "P", "A", "S", "D", "E", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "1", "2","3", "4", "5", "6", "7","8", "9", "0", "#", "@", "&", "*"]

while True:
    passward=""
    length= int(input("\nEnter the Length of Passward: "))
    for i in range (0, length, 1):
        char= random.choice (characters)
        passward=passward+char
    print("Your passward is :- ",passward)
    play_again= input ("Do you want to try again? (yes/no): \n").lower()
    if play_again  !="yes":
        break
print("THANKYOU !!!")
