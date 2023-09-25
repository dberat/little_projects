import random
import sys

correct_number = random.randint(0, 10)

attempt_liste = []
attempt = 0

start = input("Would you like to play a game?(yes/no): ")

if start.lower() == "yes":
    print("Welcome to my game...")


    while True:

        number = input("Enter a number between 0-10: ")


        def control(number, correct_number):

            if correct_number < int(number):
                return (correct_number - int(number)) * -1
            else:
                return (correct_number - int(number))


        if not number.isdigit():
            print("Lütfen sadece sayı değeri giriniz.")


        elif control(number, correct_number) == 0:
            print("Tebrikler")
            attempt += 1

            break

        elif control(number, correct_number) == 1:
            print("Dibindesin")
            attempt += 1

        elif control(number, correct_number) == 2:
            print("Yaklaştın!")
            attempt += 1

        elif control(number, correct_number) == 3:
            print("{} fark var...".format(control(number, correct_number)))
            attempt += 1

        elif control(number, correct_number) == 4:
            print("{} fark var...".format(control(number, correct_number)))
            attempt += 1

        else:
            print("Uçurum var arada...")
            attempt += 1


    print("You have found the number I guessed in {}. attempt".format(attempt))

else:
    print("Have a good day...")
    sys.exit()

