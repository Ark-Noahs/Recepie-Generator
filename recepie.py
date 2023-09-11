
'''
the following code is a recepie generator that asks the user what type of food they are craving. 
From there it prints out different options from that category. 
there are set lines to printout based off of what option user enters

future goal: expand from this, want to add different categories such as grilling, 
    baking and more. As well as add 10 different ethnic foods and offer 3 course meals as well as offer choices from breakfast, 
    lunch and dinner.
    check back at end of 2023 fall semester for updated code!
'''




#main menu
menu = {
    '1' : "American",
    '2' : "Tex-Mex",
    '3' : "Italian",
    '4' : "Asian",
    '5' : "Surprise me"
}

# Define the American menu
americanMenu = {
    '1': "Cheeseburgers with fries",
    '2': "Hot Dogs with Chili",
    '3': "Steak with mashed Potatoes",
    '4': "Lemon Pepper Wings with Waffle fries",
    '5': "Chicken fried Steak",
    '6': "Go Back"#Option to go back to the previous menu
}

texMexMenu = {
    '1': "Baja shrimp tacos",
    '2': "Classic Fajita Beef burrito",
    '3': "Ground Beef Nachos",
    '4': "Spicy Pork Chimichanga",
    '5': "Fajita Chicken plate w rice and beans ",
    '6': "Go Back"
}

italianMenu = {
    '1': "Pepperoni Pizza",
    '2': "Spaghetti and Meatballs",
    '3': "Lasagna",
    '4': "Chicken Tortellini",
    '5': "Chicken Alfredo",
    '6': "Go Back"
}


asianMenu = {
    '1': "California Roll",
    '2': "Stir Fry",
    '3': "Shrimp Fried rice",
    '4': "Vegan steamed Dumplings",
    '5': "Pho Ga Nuong",
    '6': "Go Back"
}


supriseMenu = {
    '1': "Cajun Chicken pasta",
    '2': "Pumpkin Bread",
    '3': "Japanese fluffy pancakes",
    '4': "Mango Lassi",
    '5': "Butter Chicken with rice",
    '6': "Go Back"
}



# Function to handle American menu
def handle_american_menu():
    print("\nAmerican")
    
    while True:
        americanOptions = list(americanMenu.keys())
        americanOptions.sort()
        
        for entry in americanOptions:
            print(entry, americanMenu[entry])
        
        americanSelection = input("\nPlease Select an option for American:")
        
        if americanSelection in americanMenu:  # Check if it's a valid option
            if americanSelection == '6':
                break  # Go back to the previous menu
            print("\n")
            file_name = 'file1.txt'
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                

                menu_actions = {
                    '1': (0, 46),  # cheeseburger/fries
                    '2': (49, 94),  # hotdog w chili
                    '3': (98, 148), #steak w mashed potatoes
                    '4': (150, 210),#lemon pepper wings w waffle fries
                    '5': (212, 267),#chicken fried steak
                }
                
                if americanSelection in menu_actions:
                    lines_range = menu_actions[americanSelection]
                    
                    for line in lines[lines_range[0]:lines_range[1]]:
                        print(line.strip())
                else:
                    print("Invalid selection.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            handle_user_choice()  
        else:
            print("Invalid selection. Please try again.")

# Function to handle Tex-Mex menu
def handle_TexMex_menu():
    print("\nTexMex")
    
    while True:
        texMexOptions = list(texMexMenu.keys())
        texMexOptions.sort()
        
        for entry in texMexOptions:
            print(entry, texMexMenu[entry])
            
        texMexSelection = input("\nPlease select one of the following Tex Mex dishes:")
        if texMexSelection in texMexMenu:
            if texMexSelection == '6':
                break
            print("\n")
            file_name = 'file1.txt'
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()

                menu_actions = {
                    '1': (271, 326),# baja tacos
                    '2': (330, 391), # fajita beef burrito 
                    '3': (395, 445), #beef nachos 
                    '4': (450, 506),#spicy pork chimichanga
                    '5': (509, 578),#Fajita Chicken plate w rice/beans
                }    
                if texMexSelection in menu_actions:
                    lines_range = menu_actions[texMexSelection]
                    
                    # Print lines from txt file
                    for line in lines[lines_range[0]:lines_range[1]]:
                        print(line.strip())
                else:
                    print("Invalid selection.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            handle_user_choice()  
        else:
            print("Invalid selection. Please try again.")



# Function to handle Italian menu
def handle_Italian_menu():
    print("\nItalian")
    
    while True:
        italianOptions = list(italianMenu.keys())
        italianOptions.sort()
        
        for entry in italianOptions:
            print(entry, italianMenu[entry])
            
        italianSelection = input("\nPlease select one of the following Italian dishes:")
        if italianSelection in italianMenu:
            if italianSelection == '6':
                break
            print("\n")
            file_name = 'file1.txt'
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()

                menu_actions = {
                    '1': (583, 632),# Pepperoni pizza
                    '2': (635, 697), #  spaghetti w/ meatballs
                    '3': (701, 762), #lasagna
                    '4': (766, 817),#chicken tortellini
                    '5': (822, 878),#chicken alfredo
                }    
                if italianSelection in menu_actions:
                    lines_range = menu_actions[italianSelection]

                    for line in lines[lines_range[0]:lines_range[1]]:
                        print(line.strip())
                else:
                    print("Invalid selection.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            handle_user_choice()  
        else:
            print("Invalid selection. Please try again.")
            
            
            
# Function to handle Asian menu
def handle_Asian_menu():
    print("\nAsian")
    
    while True:
        asianOptions = list(asianMenu.keys())
        asianOptions.sort()
        
        for entry in asianOptions:
            print(entry, asianMenu[entry])
            
        asianSelection = input("\nPlease select one of the following Asian dishes:")
        if asianSelection in asianMenu:
            if asianSelection == '6':
                break
            print("\n")
            file_name = 'file1.txt'
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()

                menu_actions = {
                    '1': (882, 932),#california roll
                    '2': (936, 990),#stir fry 
                    '3': (994, 1037),#shrimp fried rice 
                    '4': (1041, 1094),#vegan steam dumplings
                    '5': (1098, 1160),#Pho Ga Nuong
                }    
                if asianSelection in menu_actions:
                    lines_range = menu_actions[asianSelection]
                    
                    # Print lines from txt file
                    for line in lines[lines_range[0]:lines_range[1]]:
                        print(line.strip())
                else:
                    print("Invalid selection.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            handle_user_choice()  
        else:
            print("Invalid selection. Please try again.")



# Function to handle Suprise menu
def handle_Suprise_menu():
    print("\nSo your undecisive on what you wanna eat?\nnot to worry here are a few meals that i had my classroom vote on\n(I reccomened the Cajun Chicken Pasta if you like spicy foods)\n")
    
    while True:
        supriseOptions = list(supriseMenu.keys())
        supriseOptions.sort()
        
        for entry in supriseOptions:
            print(entry, supriseMenu[entry])
            
        supriseSelection = input("\nPlease select one of the following dishes:")
        if supriseSelection in supriseMenu:
            if supriseSelection == '6':
                break
            print("\n")
            file_name = 'file1.txt'
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                # Define menu actions with ranges from users input
                menu_actions = {
                    '1': (1164, 1219), #cajun chicken pasta 
                    '2': (1222, 1273), #pumpkin bread 
                    '3': (1277, 1329), #japanese fluffy bread
                    '4': (1333, 1365), #mango lassi
                    '5': (1368, 1431), #butter chicken w rice
                }    
                if supriseSelection in menu_actions:
                    lines_range = menu_actions[supriseSelection]
                    
                    # Print lines from txt file
                    for line in lines[lines_range[0]:lines_range[1]]:
                        print(line.strip())
                else:
                    print("Invalid selection.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            handle_user_choice()  
        else:
            print("Invalid selection. Please try again.")



def handle_user_choice():#funct:asks the user to quit or return to previous subMenu
    while True:
        return_or_end = input("\nDo you want to go back to the previous menu (menu) or end the program (end)? ")
        if return_or_end == 'menu':
            break
        elif return_or_end == 'end':
            exit()
        else:
            print("Invalid input. Please enter 'menu' or 'end'.")


while True:                                                         #Main starts 
    options = list(menu.keys())
    options.sort()
    print("Welcome to this recepie generator select one of the following to get started(1-6)")
    for entry in options:
        print(entry, menu[entry])
    print("Type out 'quit' to end program")
    selection = input("what are you craving today? ")

    if selection == '1':
        handle_american_menu()#American menu selected

    elif selection == '2':                                         
        handle_TexMex_menu() #Tex Mex menu selected 

    elif selection == '3':                                          
        handle_Italian_menu()#Italian menu selected

    elif selection == '4':                                           
        handle_Asian_menu()#Asian menu selected
        
    elif selection == '5':                                         
        handle_Suprise_menu()#suprise menu selected 
        
    elif selection == 'quit':#ends the program
        break
    else:
        print("Unknown Option Selected!")
        
