from solution import *

# run this file
choice = ''
while choice != '0':
    print("Welcome! What would you like to do?\n0. Quit\n1. Find mean color\n2. Find most worn color\n3. Find median color\n4. Get variance\n5. Color Probability\n6. Save to color and frequency database\n7. Recursive search\n8. Binary generator\n9. Fibonacci(50)\n")
    choice = input()
    if choice == '1':
        print(mean_color())
    elif choice == '2':
        print(mode_color())
    elif choice =='3':
        print(mode_color())
    elif choice =='4':
        print(variance_color())
    elif choice =='5':
        print(probability_color())
    elif choice =='6':
        print(save_to_db())
    elif choice =='7':
        print(binary_search())
    elif choice =='8':
        print(num_generator())
    elif choice =='9':
        fibs = [fib(n) for n in range(50)]
        print(fibs)
    elif choice =='0':
        print("goodbye")
    else:
        print("invalid selections, try again\n")