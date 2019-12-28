from random_interval import *

def execute_exercises():
    do_again = True

    while do_again == True:
        print("how many of each exercise do you want to generate?")
        input1 = int(input()) 
        
        chord_notes(input1)

        do_intervals(input1,"sing")

        print("Generate another batch? 'y' or 'n' ")
        repeat = str(input()) 

        if repeat == 'y':
            do_again = True
        elif repeat == 'n':
            do_again = False

if __name__ == "__main__":
    execute_exercises()