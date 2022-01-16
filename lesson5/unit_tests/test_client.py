import unittest
from common.settings import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from client import presence_to_server, check_answer

class TestClass(unittest.TestCase):

    def test_def_presense(self):
        test = presence_to_server()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        self.assertEqual(check_answer({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        self.assertEqual(check_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        self.assertRaises(ValueError, check_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()