from define_if_prime import is_prime
from sort_sequence import sort_seq
from delete_text import delete

if __name__ == '__main__':
    run = True
    while run:
        print("1) Define is number prime or not\n2) Sort sequence\n3) Delete text in brackets from string\n0) Exit")
        choice = input(">> ")

        if choice == "1":
            print("Enter a number (from 0 to 1000): ")
            number = int(input())
            if number >= 0 and number <= 1000:
                if is_prime(number):
                    print ("Number is prime")
                else:
                    print ("Number is not prime")
            else:
                print("Your number is out of range")
        elif choice == "2":
            seq = [20, 7, 14, 9, 0, -4, 15, 81, 6, -17]
            print("Unsorted sequence: ", seq)
            print ("Sorted sequence: ", sort_seq(seq))
        elif choice == "3":
            print("Enter text: ")
            txt = input()
            print("Modified text: ", delete(txt))
        elif choice == "0":
            run = False
