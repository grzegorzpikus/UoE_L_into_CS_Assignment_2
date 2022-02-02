
def Luhn(num):
    """The function checks if a credit card number is valid.
    The Luhn algorithm."""

    num = str(num)
    sum = 0
    for i in range(0, len(num)-1, 2):
        if int(num[i]) * 2 >= 10:
            temp = str(int(num[i]) * 2)
            sum_temp = int(temp[0]) + int(temp[1])
            sum += sum_temp
        else:
            sum += (int(num[i]) * 2)

    for i in range(1, len(num)+1, 2):
        sum += int(num[i])

    if sum % 10 == 0:
        return True
    else:
        return False


class Card:
    """The class that creates a single card details instance."""

    def __init__(self, first_name, surname, number, cvv, exp_date):
        self.first_name = first_name
        self.surname = surname
        self.number = number
        self.cvv = cvv
        self.exp_date = exp_date


    def __repr__(self):
        return f'{self.first_name} {self.surname}, card number: ' \
               f'{self.number}, CVV: {self.cvv}, expiry date: {self.exp_date}'

    # this __eq__ method had to be modified to compare graphical representation
    # of two instances of Card Class, needed for Unittests.
    def __eq__(self, other):
        if isinstance(other, self.__class__):

            if other.first_name != self.first_name:
                return False
            if other.surname != self.surname:
                return False
            if other.number != self.number:
                return False
            if other.cvv != self.cvv:
                return False
            if other.exp_date != self.exp_date:
                return False
            return True
        else:
            return self.__dict__ == other.__dict__



