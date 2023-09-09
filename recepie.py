

#     UPDATED: 09/09   rewrote code so that its simpler to read
#    -stopped at American menu (1) , option 3



#main menu
menu = {}
menu['1'] = "American"
menu['2'] = "Tex-Mex"
menu['3'] = "Italian"
menu['4'] = "Asian"
menu['5'] = "Surprise me"

# Define the American menu
americanMenu = {}
americanMenu['1'] = "CheeseBurgers with fries"
americanMenu['2'] = "HotDogs with chili"
americanMenu['3'] = "Steak with mashed potatoes"
americanMenu['4'] = "Lemon Pepper Wings with waffle fries"
americanMenu['5'] = "Chicken fried Steak"
americanMenu['6'] = "Go Back"# Option to go back to the previous menu

while True:
    options = list(menu.keys())
    options.sort()
    print("Welcome to this recepie generator select one of the following to get started(1-6)")
    for entry in options:
        print(entry, menu[entry])
    print("Type out 'quit' to end program")

    selection = input("what are you craving today? ")

    if selection == '1':                                #American menu selected
        print("\nAmerican")
        # Display the American menu
        while True:
            americanOptions = list(americanMenu.keys())
            americanOptions.sort()

            for entry in americanOptions:
                print(entry, americanMenu[entry])

            americanSelection = input("\nPlease Select an option for American:").lower()

            if americanSelection == '1':#cheeseburger/fries
                print("\n")
                file_name = 'file1.txt'
                try:
                    with open(file_name, 'r') as file:
                        lines = file.readlines()
                # Print lines from txt file w/o line numbers
                        for line in lines[:46]:
                            print(line.strip())
                except FileNotFoundError:
                    print(f"File '{file_name}' not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
        
            
                while True:#option to fo to American menu or end the program
                    return_or_end = input("\nDo you want to go back to the previous menu (menu) or end the program (end)? ")
                    if return_or_end == 'menu':
                        break
                    elif return_or_end == 'end':
                        exit()
                    else:
                        print("Invalid input. Please enter 'menu' or 'end'.")

            elif americanSelection == '2':#hotdog w chili
                print("\n")
                file_name = 'file1.txt'
                try:
                    with open(file_name, 'r') as file:
                        lines = file.readlines()
                #prints lines 45-94        
                        for line in lines[49:94]:
                            print(line.strip())
                except FileNotFoundError:
                    print(f"file '{file_name}' not found.")
                except Exception as e:
                    print(f"An error has occured: {e}")
                
                while True:
                    return_or_end = input("\nDo you want to go back to the previous menu (menu) or end the program (end)? ")
                    if return_or_end == 'menu':
                        break
                    elif return_or_end == 'end':
                        exit()
                    else:
                        print("Invalid input. Please enter 'menu' or 'end'.")                
                
            elif americanSelection == '3':#Steak w/ mashed potatoes
                print("\n")
                file_name = 'file1.txt'
                try:
                    with open(file_name, 'r') as file:
                        lines = file.readlines()
                        #lines 97-148
                        for line in lines[97:148]:
                            print(line.strip())
                except FileNotFoundError:
                    print(f"file '{file_name}' not found ")
                except Exception as e:
                    print(f"an error has occured: {e}")
                #ADD CODE SO THAT IT ASKS TO SELECT ANOTHER OPTION OR QUIT PROGRAM
                
                
                
                
                
                
                
            elif americanSelection == '4':
                print("Lemon Pepper Wings with waffle fries")
                # Your code for making Lemon Pepper Wings with waffle fries goes here
            elif americanSelection == '5':
                print("Chicken fried Steak")
                # Your code for making Chicken fried Steak goes here
            elif americanSelection == '6':
                break  # Go back to the previous menu
            
            else:
                print("Unknown Option Selected in American Menu!Please select one of the following\n")

#work on this code once you get the top part running how you like it        
    elif selection == '2':                                          #Tex Mex menu selected 
        print("\nTex-Mex")
        # Your code for deleting a student goes here
    elif selection == '3':                                          #Italian menu selected
        print("\nItalian")
        # Your code for finding a student goes here
    elif selection == '4':                                          #Asian menu selected 
        print("\nAsian")
    elif selection == '5':                                          #suprise menu selected 
        print("\nSurprise me")
        
    elif selection == 'quit':#ends the program
        break
    else:
        print("Unknown Option Selected!")

