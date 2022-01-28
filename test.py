import csv
from Card_calss import Card
fn = 'John'
sn = 'Smith'

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

search_name(fn, sn)