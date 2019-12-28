from random_interval import *

def execute_exercises():
    print("how many of each exercise do you want to generate?")
    input1 = int(input()) 
    
    chord_notes(input1)

    do_intervals(input1,"sing")

if __name__ == "__main__":
    execute_exercises()