import unittest

def sort_list(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j+1] = input_list[j + 1], input_list[j]
    return input_list

class TestSortList(unittest.TestCase):

    def test_sort_list(self):
        # Prueba con una lista desordenada
        unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_list = sort_list(unsorted_list)
        self.assertEqual(sorted_list, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()