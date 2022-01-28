from manage import print_all, search_name, search_card, add_card, delete_card, \
    my_sort


def menu():
    """Navigation menu and executing functionalities of the application."""

    print('=' * 38 + ' Menu ' + '=' * 38)
    print('=' * 30 + ' Choose a menu option ' + '=' * 30)
    print(' 1. Inspect \n 2. Search for card details. '
          '\n 3. Add new card details. '
          '\n 4. Delete existing card details. '
          '\n 5. Back to the main menu'
          '\n 6. Exit')


    while True:
        command = int(input('Enter menu option number: '))

        if command == 6:
            print('=' * 82)
            print('You have quit the application.')
            print('=' * 82)
            exit()

        elif command == 5:
            menu()

        elif command == 1:
            print('=' * 36 + ' Inspect ' + '=' * 37)
            print('In the option 2 you can:'
                  '\n <*> print all cart details stored in the system [-p]. '
                  '\n <*> print all cart details stored in the system sorted by name [-sap]. '
                  '\n <*> search for card details based on name of a card holder [-n]. '
                  '\n <*> search for cart details based on a card number [-n].'
                  '\nIn the option 3 you can:'
                  '\n <*> add new card details'
                  '\nIn the option 4 you can:'
                  '\n <*> delete card details based on name of a card holder [-n].'
                  '\n <*> delete card tetails baded on a card number [-c]')

        elif command == 2:
            print('=' * 37 + ' Search ' + '=' * 37)
            print(' <*> print all cart details stored in the system by typing \'-p\' '
                  '\n <*> print all cart details stored in the system sorted by name by typin \'-sap\'. '
                  '\n <*> search for card details based on name of a card holder \'-n\'. '
                  '\n <*> search for cart details based on a card number \'-c\'.'
                  '\n <*> back to the main menu by typing \'-e\'')

            while True:
                search_input = input('Enter your choice: ')
                if search_input == '-e':
                    menu()
                elif search_input == '-p':
                    print('-' * 80)
                    print_all()
                    print('-' * 80)
                elif search_input == '-n':
                    search_input_name = str(input('Enter first name and last name of a card holder (separated by space): '))
                    name = search_input_name.split()
                    first_name = (name[0].lower()).capitalize()
                    surname = (name[1].lower()).capitalize()
                    print('-' * 80)
                    search_name(first_name, surname)
                    print('-' * 80)
                elif search_input == '-c':
                    try:
                        search_input_card = int(input('Enter card number: '))
                        print('-' * 80)
                        search_card(search_input_card)
                        print('-' * 80)
                    except ValueError:
                        print("That was invalid number. Please try again.")
                elif search_input == '-sap':
                    my_sort()
                else:
                    print('-' * 82)
                    print('Wrong command, try again.')
                    print('-' * 82)

        elif command == 3:
            print('=' * 37 + ' Add ' + '=' * 39)

            while True:
                fn = str(input('Enter first name of a card holder (type \'-e\' for returning to the main menu): '))
                if fn == '-e':
                    menu()
                sn = str(input('Enter last name of a card holder (type \'-e\' for returning to the main menu): '))
                if sn == '-e':
                    menu()
                cn = ''
                try:
                    cn = int(input('Enter card number (type \'0\' for returning to the main menu): '))
                except ValueError:
                    print('-' * 82)
                    print("That was invalid number. Please try again.")
                    print('-' * 82)
                    break
                if cn == 0:
                    menu()
                cvv = str(input('Enter CVV (type \'-e\' for returning to the main menu): '))
                if cvv == '-e':
                    menu()
                ed = str(input('Enter expiry date as \'XX/XX\' (type \'-e\' for returning to the main menu): '))
                if ed == '-e':
                    menu()
                rc = str(input('Premission for holding card details (type Y or N) (type \'-e\' for returning to the main menu): '))
                if rc == '-e':
                    menu()

                x = add_card(fn, sn, cn, cvv, ed, rc)

                if x == True:
                    print('-' * 82)
                    print("The card details have been successfully added.")
                    print('-' * 82)

        elif command == 4:
            print('=' * 37 + ' Delete ' + '=' * 37)
            print(' <*> delete chosen cart details stored in the system:'
                  '\n <*> based on cart number by typing \'-c\'.'
                  '\n <*> back to the main menu by typing \'-e\'.')

            while True:
                delete_input = input('Enter your choice: ')
                if delete_input == '-e':
                    menu()
                elif delete_input == '-c':
                    try:
                        delete_input_card = int(input('Enter card number: '))
                        x = delete_card(delete_input_card)
                        if x == True:
                            print('-' * 82)
                            print('The card details have been removed successfully.')
                            print('-' * 82)
                        else:
                            print('-' * 82)
                            print(x)
                            print('-' * 82)
                    except ValueError:
                        print('-' * 82)
                        print("That was invalid number. Please try again.")
                        print('-' * 82)
                else:
                    print('-' * 82)
                    print('Wrong command, try again.')
                    print('-' * 82)

        else:
            print('=' * 82)
            print('Wrong command. Please try again.')
            print('=' * 82)


if __name__ == '__main__':
    menu()
