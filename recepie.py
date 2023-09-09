

#update 09/08


def submenu_option_1():             #1-47
    print("You selected CheeseBurgers with fries.")
    file_name = 'file1.txt' 
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            # Print lines 1 to 14 without line numbers
            for line in lines[:45]:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def submenu_option_2():         #48-91
    print("You selected HotDogs with chili")

def submenu_option_3():         #95-120
    print("You selected Steak with mashed potatoes")

def submenu_option_4():         #146-203
    print("You selected Lemon Pepper Wings with waffle fries")

def submenu_option_5():         #206-258
    print("You selected Chicken fried Steak")

def submenu_option_6():                          
    print("You selected Baja shrimp tacos")
    file_name = 'file2.txt' 
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            # Print lines 15 to 29 without line numbers
            for line in lines[14:29]:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def submenu_option_7():
    print("You selected Classic Tex-Mex burriot")

def submenu_option_8():
    print("You selected Ground Beef nachos")
    # Add your code here for Sub-option 1.8

def submenu_option_9():
    print("You selected spricy pork Chimichanga")
    # Add your code here for Sub-option 1.9

def submenu_option_10():
    print("You selected Fajita chicken plate with rice/beans")
    # Add your code here for Sub-option 1.10

def submenu_option_11():
    print("You selected Pepperoni Pizza")
    # Add your code here for Sub-option 1.11

def submenu_option_12():
    print("You selected Spaghetti and Meatballs")
    # Add your code here for Sub-option 1.12

def submenu_option_13():
    print("You selected Lasagna")
    # Add your code here for Sub-option 1.13

def submenu_option_14():
    print("You selected Chicken Alfedo")
    # Add your code here for Sub-option 1.14

def submenu_option_15():
    print("You selected chicken tortellini")
    # Add your code here for Sub-option 1.15

def submenu_option_16():
    print("You selected sushi")
    # Add your code here for Sub-option 1.16

def submenu_option_17():
    print("You selected stir fry")
    # Add your code here for Sub-option 1.17

def submenu_option_18():
    print("You selected chop suey")
    # Add your code here for Sub-option 1.18

def submenu_option_19():
    print("You selected shrimp fried rice")
    # Add your code here for Sub-option 1.19

def submenu_option_20():
    print("You selected vegan steamed dumplings")
    # Add your code here for Sub-option 1.20

def submenu_option_21():
    print("You selected cajun chicken pasta")
    # Add your code here for Sub-option 1.21

def submenu_option_22():
    print("You selected pumpkin bread")
    # Add your code here for Sub-option 1.22

def submenu_option_23():
    print("You selected japanese fluffy pancakes")
    # Add your code here for Sub-option 1.23

def submenu_option_24():
    print("You selected mango lassi")
    # Add your code here for Sub-option 1.24

def submenu_option_25():
    print("You selected butter chicken with rice")
    # Add your code here for Sub-option 1.25







def display_submenu(submenu_title, submenu_options, submenu_functions):
    print(f"Submenu for {submenu_title}:")
    for key, value in submenu_options.items():
        print(f"{key}. {value}")

    sub_choice = input(f"Select a sub-option (1-5) for {submenu_title} or 'b' to go back to the previous menu: ")

    if sub_choice == 'b':
        return

    selected_function = submenu_functions.get(sub_choice)

    if selected_function:
        selected_function()
    else:
        print("Invalid sub-option.")

def display_menu(menu):
    while True:
        print("\nWhat would you like to cook today? \nThe difficulty of these dishes are in order from simple to complex")
        for key, value in menu.items():
            print(f"{key}. {value['title']}")

        choice = input("Select an option (1-5) or 'q' to quit: ")

        if choice == 'q':
            break

        submenu = menu.get(choice)

        if submenu:
            submenu_title = submenu['title']
            submenu_options = submenu['submenu']
            submenu_functions = {
                '1': submenu_option_1,
                '2': submenu_option_2,
                '3': submenu_option_3,
                '4': submenu_option_4,
                '5': submenu_option_5,
                '6': submenu_option_6,
                '7': submenu_option_7,
                '8': submenu_option_8,
                '9': submenu_option_9,
                '10': submenu_option_10,
                '11': submenu_option_11,
                '12': submenu_option_12,
                '13': submenu_option_13,
                '14': submenu_option_14,
                '15': submenu_option_15,
                '16': submenu_option_16,
                '17': submenu_option_17,
                '18': submenu_option_18,
                '19': submenu_option_19,
                '20': submenu_option_20,
                '21': submenu_option_21,
                '22': submenu_option_22,
                '23': submenu_option_23,
                '24': submenu_option_24,
                '25': submenu_option_25,
    }

            
            display_submenu(submenu_title, submenu_options, submenu_functions)
        else:
            print("Invalid option. Please select a valid option (1-2) or 'b' to go back to the previous menu.")

if __name__ == "__main__":
    main_menu = {
        '1': {
            'title': 'American',
            'submenu': {
                '1': 'CheeseBurgers with fries',
                '2': 'HotDogs with chili',
                '3': 'Steak with mashed potatoes',
                '4': 'Lemon Pepper Wings with waffle fries',
                '5': 'Chicken fried Steak',
            }
        },
        
        '2': {
            'title': 'Tex-Mex',
            'submenu': {
                '6': 'Baja shrimp tacos',
                '7': 'Classic Fajita beef burrito',
                '8': 'Ground Beef nachos',
                '9': 'chimichanga',
                '10': 'Fajita chicken plate with rice/beans',
            }
        },
        '3': {
            'title': 'Italian',
            'submenu': {
                '1': 'Pepperoni Pizza',
                '2': 'Spaghetti and Meatballs',
                '3': 'Lasagna',
                '4': 'Chicken Alfredo',
                '5': 'Chicken Tortelini',
            }
        },
        '4': {
            'title': 'Asian',
            'submenu': {
                '1': 'Sushi:California roll',
                '2': 'Stir Fry',
                '3': 'Chop Suey',
                '4': 'Shrimp fried rice',
                '5': '(Chicken/Vegan)(fried/steamed) Dumplings ',
            }
        },
        '5': {
            'title': 'Suprise Me',
            'submenu': {
                '1': 'Cajun chicken pasta',
                '2': 'Pumpkin Bread',
                '3': 'Japanese Fluffy pancakes',
                '4': 'Mango Lassi',
                '5': 'Butter Chicken',
            }
        },
        
    }

    display_menu(main_menu)
