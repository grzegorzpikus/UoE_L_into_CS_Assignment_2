import csv
from Data_validation import initial_test
from Card_calss import Luhn, Card
from sorting import quick_sort


def print_all():
    """The function prints all credit card details stored in the CSV file."""

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(Card(row[1], row[2], row[3], row[4], row[5]))
    file.close()


def search_name(fn, sn):
    """The function searches for details of a chosen card by first name and
    surname name of a card holder in the CSV file."""

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        list_of_cards = []
        for row in reader:
            if row[1] == fn and row[2] == sn:
                list_of_cards.append(Card(row[1], row[2], row[3], row[4],
                                          row[5]))
    file.close()
    if list_of_cards == []:
        return 'Card not found'
    else:
        for i in list_of_cards:
            print(i)
        for i in list_of_cards:
            return i


def search_card(cn):
    """The function searches for details of a chosen card by first name and
    surname name in the CSV file."""

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        status = False
        for row in reader:
            if row[3] == str(cn):
                d = Card(row[1], row[2], row[3], row[4], row[5])
                status = True

    file.close()
    if status is False:
        return 'Card not found'
    else:
        print(d)
        return d


def search_index_name(fn, sn):
    """Function returns index of card details in CSV file based on name."""

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        status = False
        for row in reader:
            if row[1] == fn and row[2] == sn:
                status = row[0]
    file.close()
    return status


def search_index_card(cn):
    """Function returns index of card details in CSV file based on card no."""

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        status = False
        for row in reader:
            if row[3] == str(cn):
                status = row[0]
    file.close()
    return status


def add_card(fn, sn, cn, cvv, ed, rc):
    """The function adds nwe card details to CSV file."""

    if initial_test(fn, sn, cn, cvv, ed, rc) is False:
        return False
    if Luhn(cn) is False:
        print('-' * 82)
        print('Invalid card number')
        print('-' * 82)
        return False

    if search_index_card(cn) is not False:
        print('-' * 82)
        print('The Card already exists.')
        print('-' * 82)
        return False

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        list_index = []
        for row in reader:
            index = int(row[0])
            list_index.append(index)
        last_index = max(list_index)
        file.close()

    new_row = [(last_index + 1)]
    new_row.append(fn)
    new_row.append(sn)
    new_row.append(cn)
    new_row.append(cvv)
    new_row.append(ed)

    with open('data.csv', 'a', newline='') as file2:
        writer = csv.writer(file2)
        writer.writerow(new_row)
    file2.close()
    return True


def delete_card(cn):
    """The functions deletes card details based on the card number."""

    if search_index_card(cn) is False:
        return 'no card found'
    else:
        index = int(search_index_card(cn))

    with open('data.csv', 'r') as output_file, \
            open('copy_data.csv', 'w', newline='') as input_file:
        reader = csv.reader(output_file)
        writer = csv.writer(input_file)

        for row in reader:
            if int(row[0]) < index:
                writer.writerow(row)
            elif int(row[0]) == index:
                pass
            else:
                new_index = int(row[0])
                new_index -= 1
                row[0] = str(new_index)
                writer.writerow(row)

        output_file.close()
        input_file.close()

    import os

    os.remove("data.csv")
    os.rename("copy_data.csv", "data.csv")

    return True


def my_sort():
    """The function sort by surname and print all card details stored in a CSV
    file."""

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        list_of_cards = []
        for row in reader:
            list_of_cards.append(Card(row[1], row[2], row[3], row[4], row[5]))
    file.close()

    list_of_surnames = []
    for i in list_of_cards:
        list_of_surnames.append(i.surname)

    quick_sort(list_of_surnames, 0, len(list_of_surnames)-1)

    for i in list_of_surnames:
        for j in list_of_cards:
            if i == j.surname:
                x = list_of_cards.pop(list_of_cards.index(j))
                print(x)



