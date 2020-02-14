import unittest
from pandas import Timestamp

from get_dividends import modify_dividends

class TestControl(unittest.TestCase):

    def test_control_add(self):
        self.assertEqual(2, 1+1)

class TestGetDividends(unittest.TestCase):

    maxDiff = None

    def test_modify_dividends_simple(self):
        dividend_history = [{'Amount': 1, 'Type': 'Dividend', 'Date': Timestamp(2000, 01, 01)},
                            {'Amount': 2, 'Type': 'Dividend', 'Date': Timestamp(2001, 01, 01)},
                            {'Amount': 2, 'Type': 'Split', 'Date': Timestamp(2002, 01, 01)}]
        modified_dividend_history = [{'Amount': 0.5, 'Type': 'Dividend', 'Date': Timestamp(2000, 01, 01)},
                                     {'Amount': 1.0, 'Type': 'Dividend', 'Date': Timestamp(2001, 01, 01)}]
        self.assertEqual(modify_dividends(dividend_history), modified_dividend_history)

    def test_modify_dividends(self):
        dividend_history = [{'Amount': 1, 'Type': 'Dividend', 'Date': Timestamp(2000, 01, 01)},
                            {'Amount': 2, 'Type': 'Dividend', 'Date': Timestamp(2001, 01, 01)},
                            {'Amount': 2, 'Type': 'Split', 'Date': Timestamp(2002, 01, 01)},
                            {'Amount': 1, 'Type': 'Dividend', 'Date': Timestamp(2003, 01, 01)},
                            {'Amount': 0.5, 'Type': 'Split', 'Date': Timestamp(2004, 01, 01)},
                            {'Amount': 1, 'Type': 'Dividend', 'Date': Timestamp(2005, 01, 01)},
                            {'Amount': 4, 'Type': 'Split', 'Date': Timestamp(2006, 01, 01)},
                            {'Amount': 1, 'Type': 'Dividend', 'Date': Timestamp(2007, 01, 01)}]
        modified_dividend_history = [{'Amount': 0.25, 'Type': 'Dividend', 'Date': Timestamp(2000, 01, 01)},
                                     {'Amount': 0.5, 'Type': 'Dividend', 'Date': Timestamp(2001, 01, 01)},
                                     {'Amount': 0.5, 'Type': 'Dividend', 'Date': Timestamp(2003, 01, 01)},
                                     {'Amount': 0.25, 'Type': 'Dividend', 'Date': Timestamp(2005, 01, 01)},
                                     {'Amount': 1.0, 'Type': 'Dividend', 'Date': Timestamp(2007, 01, 01)}]
        self.assertEqual(modify_dividends(dividend_history), modified_dividend_history)
        
if __name__ == '__main__':
    unittest.main()

