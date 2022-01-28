import unittest
import Card_calss
import manage
import sorting

class TestLuhn(unittest.TestCase):

    def test_Luhn(self):
        result_valid = Card_calss.Luhn(6703444444444449)
        self.assertEqual(result_valid, True)
        result_invalid = Card_calss.Luhn(6703444444444441)
        self.assertEqual(result_invalid, False)

    def test_search_name(self):
        result_name = manage.search_name('Gorge', 'Tones')
        gorge_tones = Card_calss.Card('Gorge', 'Tones', '5105105105105100',
                                     '406', '04/26')
        self.assertEqual(result_name, gorge_tones)

        result_no_name = manage.search_name('Eve', 'McDnald')
        eve_macdonald = 'Card not found'
        self.assertEqual(result_no_name, eve_macdonald)

    def test_search_card(self):
        result_card = manage.search_card(5105105105105100)
        gorge_tones = Card_calss.Card('Gorge', 'Tones', '5105105105105100',
                                    '406', '04/26')
        self.assertEqual(result_card, gorge_tones)

        result_no_number = manage.search_card(5555341244441115)
        number = 'Card not found'
        self.assertEqual(result_no_number, number)

    def test_quick_sort(self):
        import random
        import string

        strs_list = []
        for i in range(10):
            letters = string.ascii_lowercase
            strs_list.append(''.join(random.choice(letters) for j in range(4)))

        my_sorting = sorting.quick_sort(strs_list, 0, len(strs_list)-1)
        python_sorting = sorted(strs_list)
        self.assertEqual(my_sorting, python_sorting)

if __name__ == '__main__':
    unittest.main()

