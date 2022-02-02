from datetime import date


def name_test(fn, sn):
    """The function checks if first name and surname are strings containing
    letters only."""

    def has_numbers(sting):
        """The function checks every character in a string
        to examine whether it is a digit"""
        return any(char.isdigit() for char in sting)

    if has_numbers(fn) is True:
        return 'Wrong first name'
    if has_numbers(sn) is True:
        return 'Wrong surname'
    return True


def card_number_test(cn):
    """The function checks if card number is 16-digit number."""

    cn = str(cn)
    if len(cn) != 16:
        return 'Wrong card number'
    else:
        return True


def cvv_test(cvv):
    """The function checks if cvv is 3-digit number."""

    if cvv.isnumeric() is False:
        return 'Wrong cvv'

    if len(cvv) != 3:
        return 'Wrong cvv'
    else:
        return True


def expiry_date_test(ed):
    """The function checks if the expiry date is correct"""

    if len(ed) != 5:
        return 'Wrong expiry date'
    elif ed[2] != '/':
        return 'Wrong expiry date'
    else:
        month_year = ed.split('/')
        month = month_year[0]
        year = month_year[1]
        if int(month) > 12:
            return 'Wrong expiry date (moth)'
        if int(year) == date.today().year - 2000:
            if int(month) > date.today().month:
                return 'Wrong expiry date (year)'

        return True


def regular_customer_test(rc):

    if rc != 'N':
        if rc !='Y':
            return 'Press correct letter Y or N'
    if rc == 'N':
        return 'Card details cannot be stored!'

    return True



def initial_test(fn, sn, cn, cvv, ed, rc):
    """The function invokes all initial test functions.
    a = result of name_test()
    b = result of card_number_test()
    c = result of cvv_test()
    d = result of expiry_date_test()
    e = result of regular_customer_test"""

    a = name_test(fn, sn)
    b = card_number_test(cn)
    c = cvv_test(cvv)
    d = expiry_date_test(ed)
    e = regular_customer_test(rc)

    # In a list below the function collects the result of all tests.
    # If at least one of them is not True but a message, the initial test
    # is not passed and it shows message what was wrong with data
    # that were passed through.
    list_of_results = [a, b, c, d, e]
    output = ''

    for i in list_of_results:
        if i is not True:
            output += i + '; '

    if output != '':
        print('-' * 82)
        print(output)
        print('Please try again.')
        print('-' * 82)
        return False
    else:
        return True










