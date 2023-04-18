from define_if_prime import is_prime

if __name__ == '__main__':
    run = True
    while run:
        print("1) Define is number prime or not\n0) Exit")
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
        elif choice == "0":
            run = False
