while True:
    
    try:
        num_leds = int(input("Enter the number of LEDs to switch on (1-10): "))
        
        
        if 1 <= num_leds <= 10:

            for i in range(1, num_leds + 1):
                print("LED {} is ON".format(i))
        else:
            print("Number out of range. Please enter a number between 1 and 10.")
            continue

    except ValueError:
        print("Invalid input. Please enter a valid integer number.")
        continue
    
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    if restart == 'n':
        print("Program ended.")
        break