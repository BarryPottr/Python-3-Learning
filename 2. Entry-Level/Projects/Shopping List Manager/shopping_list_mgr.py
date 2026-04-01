import json, os, subprocess

def clear_screen():
    clear = ['cls'] if os.name == 'nt' else ['clear'] # Clear terminal screen depending on OS
    subprocess.run(clear, shell=True)


def get_list():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'shopping_list_mgr.json')
    try:
        with open(json_path, 'r') as f:
            ls = json.load(f)
            return ls if isinstance(ls, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

    return ls


def save_list(shop_ls):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'shopping_list_mgr.json')
    
    with open(json_path, 'w') as f:
        json.dump(shop_ls, f)


def view_list(shop_ls):    
    print("Your List:\n")
    
    for index, item in enumerate(shop_ls): # enumerate() lets us see the index of each item in a for-loop, as well as the item itself
        print(f'{index + 1}. {item['name']} - {item['quantity']}')

    input('\nPress any key to return to the menu...')
    clear_screen()
    

def add_to_list(shop_ls):
    item_lookup = {item['name'].lower(): item for item in shop_ls}
    
    while True:
        name = input('Please enter the product name: ')

        if name.lower() in item_lookup:
            print(f'\nLooks like {name} is already on your list.')
            confirmation = input(f'Did you want to change the quantity of {name}? ')

            match confirmation.lower():
                case 'y' | 'yes' | 'yeah' | 'sure' | 'yup' | 'ok' | 'yes please':
                    new_quantity = input('\nPlease update the product quantity: ')
                    item_lookup[name.lower()]['quantity'] = new_quantity
                    print('\nQuantity updated.\n')
                    break
                case 'n' | 'no thanks' | 'nope' | 'cancel'| 'no' | 'stop':
                    print('Okay.')
                    clear_screen()
                    return shop_ls
                case _:
                    print('\nThat was an invalid input. Please try again.\n')
            
        else:
            quantity = input('Please enter the product quantity: ')
            shop_ls.append({'name': name, 'quantity': quantity})
            print(f'\n{name} successfully added to the list\n')
            break
    
    save_list(shop_ls)
    print('Saving list...\nSave successful!\n')
    input('Press any key to return to the menu...')
    clear_screen()

    return shop_ls


def remove_from_list(shop_ls):
    for index, item in enumerate(shop_ls):
        print(f'{index + 1}. {item['name']} - {item['quantity']}')

    item_to_remove = int(input('\nEnter the number of the item you want to remove: '))
    confirmation_message = f'\nAre you sure you want to remove {shop_ls[item_to_remove - 1]['name']} ' \
    'from your list? '

    while True:
        confirmation = input(confirmation_message).lower()
        match confirmation:
            case 'y' | 'yes' | 'yeah' | 'sure' | 'yup' | 'ok' | 'yes please':
                shop_ls.remove(shop_ls[int(item_to_remove) - 1])
                print('\nSuccessfully removed item\n')
                save_list(shop_ls)
                print('Saving list...\nSave successful!\n')
                input('Press any key to return to the menu...')
                clear_screen()
                return shop_ls
            case 'n' | 'no thanks' | 'nope' | 'cancel'| 'no' | 'stop':
                print('That\'s okay. The item wasn\'t removed.\n')
                input('Press any key to return to the menu...')
                clear_screen()
                return shop_ls
            case _:
                print('That was an invalid input. Please try again.\n')


def greeting_message():
    # TODO: Add ASCII text
    initial_message = 'Welcome to the Shopping Cart Manager!\n'
    print(initial_message)


def home_menu():
    shopping_list = get_list()
    
    if not shopping_list:
        print('Looks like your list is empty.\n')
        add_to_list(shopping_list)
    
    options_message = 'What would you like to do?\n\n' \
    '1. View List\n' \
    '2. Add Item to List\n' \
    '3. Remove Item From List\n' \
    '4. Exit\n\n' \
    'Please choose an option (1, 2, 3, or 4): '

    while True:
        user_choice = input(options_message) # TODO: Add handling for invalid input
        print('')

        match user_choice:
            case '1':
                if not shopping_list:
                    print('Looks like your list is empty.\n')
                    break
                clear_screen()
                view_list(shopping_list)
            case '2':
                clear_screen()
                shopping_list = add_to_list(shopping_list)
            case '3':
                if not shopping_list:
                    print('Looks like your list is empty.\n')
                    break
                clear_screen()
                shopping_list = remove_from_list(shopping_list)
            case '4':
                print('Exiting program...')
                break
            case _:
                print('That was an invalid input.')

        print('')


greeting_message()
home_menu()
