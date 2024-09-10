'''Howdy!
I wrote a python script called "add_2_numbers.py" to play around with importing my own code into other projects. 
However, whenever I try to run the program, python can't find the file I just wrote! Can you help me please?'''
import add_2_numbers

def main():
    num_one = int(input("Please give me a number between 1 and 10: "))
    num_two = int(input("Please give me another number between 1 and 10:"))
    final_sum = add_2_numbers.add_two_numbers(num_one, num_two)
    print("Your sum is", final_sum)

main()
