import unittest
from unittest.mock import patch, MagicMock

from main import len_joke,get_joke




class TestJoke(unittest.TestCase):
    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(),3)

    @patch('main.requests')
    def test_get_joke(self,mock_requests):

        mock_response =MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'setup':"What did one necrophiliac tell the other necrophiliac after work?",
                                           'delivery':"Let's go have a couple of cold ones!"}
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(),"What did one necrophiliac tell the other necrophiliac after work?Let's go have a couple of cold ones!")

    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code = 403)
        mock_response.json.return_value = mock_response
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "No jokes")


if __name__ =='__main__':
    unittest.main()