from pedigree_matrix import PedigreeMatrix
from pedigree_matrix.from_string import find_pedigree_matrix as fpm
import unittest

# class InputTest(unittest.TestCase):
#     def test_ecospold_input(self):
#         input_text = "(1, 2, 3)"
#         pm = PedigreeMatrix(1,)
#         self.assertEqual(pm.parse_args((input_text,)), [1, 2, 3])

#     def test_float_inputs(self):
#         input_text = (1, 2, 3)
#         pm = PedigreeMatrix(1,)
#         self.assertEqual(pm.parse_args((input_text,)), [1, 2, 3])

#     def test_str_inputs(self):
#         input_text = ("1", "2", "3")
#         pm = PedigreeMatrix(1,)
#         self.assertEqual(pm.parse_args((input_text,)), [1, 2, 3])

#     def test_padding(self):
#         input_text = [1, 2, 3]
#         pm = PedigreeMatrix(input_text)
#         self.assertEqual(pm.pad_args(input_text),
#             [1, 2, 3, 1, 1, 1])

#     def test_complete_parsing_ecospold_input(self):
#         input_text = "(1, 2, 3)"
#         pm = PedigreeMatrix(input_text)
#         self.assertEqual(pm.inputs, [1, 2, 3, 1, 1, 1])

#     def test_complete_parsing_float_inputs(self):
#         input_text = (1, 2, 3)
#         pm = PedigreeMatrix(input_text)
#         self.assertEqual(pm.inputs, [1, 2, 3, 1, 1, 1])

#     def test_complete_parsing_str_inputs(self):
#         input_text = ("1", "2", "3")
#         pm = PedigreeMatrix(input_text)
#         self.assertEqual(pm.inputs, [1, 2, 3, 1, 1, 1])

#     def test_denester(self):
#         input_dict = {1: {2: {3: 4}}}
#         pm = PedigreeMatrix(1,)
#         self.assertEqual(pm.denester((1, 2, 3), input_dict), 4)
#         input_dict = {1: 2}
#         pm = PedigreeMatrix(1,)
#         self.assertEqual(pm.denester((1, ), input_dict), 2)


class RegularExpressionTest(unittest.TestCase):
    def test_multiple_matrices(self):
        return
        # Only use if remove constraint that occurs at very beginning
        s = "(1,2,3,4,5,5); lorem ipsum foo bar (1,2,3,4,5,5)"
        with self.assertRaises(ValueError):
            fpm(s)

    def test_plain_string(self):
        s = "(1,2,3,4,5,5)"
        self.assertEqual(fpm(s), (1, 2, 3, 4, 5, 5))

    def test_element_padding(self):
        s = "(1,2,3,4,5)"
        self.assertEqual(fpm(s), (1, 2, 3, 4, 5, 1))

    def test_beginning_of_long_string(self):
        s = "(1,2,3,4,5,5); lorem ipsum foo bar"
        self.assertEqual(fpm(s), (1, 2, 3, 4, 5, 5))

    def test_not_found_in_middle(self):
        s = "lorem ipsum foo bar (1,2,3,4,5,5)"
        self.assertFalse(fpm(s))

    def test_with_dashes(self):
        s = "(1,-,-,3,4,5)"
        self.assertEqual(fpm(s), (1, 1, 1, 3, 4, 5))
        s = "(-,-,-,-,-,-)"
        self.assertEqual(fpm(s), (1, 1, 1, 1, 1, 1))

    def test_no_data(self):
        s = "(,,,,)"
        self.assertEqual(fpm(s), (1, 1, 1, 1, 1, 1))
        s = "(,,,,,)"
        self.assertEqual(fpm(s), (1, 1, 1, 1, 1, 1))

    def test_na(self):
        s = "(1,2,3,na,na,4)"
        self.assertEqual(fpm(s), (1, 2, 3, 1, 1, 4))

    def test_na_periods(self):
        s = "(1,2,3,n.a.,n.a,na.)"
        self.assertEqual(fpm(s), (1, 2, 3, 1, 1, 1))

    def test_all_na(self):
        s = "(na,na,na,na,na)"
        self.assertEqual(fpm(s), (1, 1, 1, 1, 1, 1))

    def test_with_spaces(self):
        s = "( 1 , 2, 3 ,4 , 5 , 5 )"
        self.assertEqual(fpm(s), (1, 2, 3, 4, 5, 5))
