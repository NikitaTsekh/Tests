from unittest import mock, TestCase
import google,facebook,data




class TestApiFirst(TestCase):
    """
    Testing 2 different fucnctions
    """

    @mock.patch('facebook.get_data', return_value='data_3')
    @mock.patch('google.get_data',return_value ='data_2')
    def test_external_api(self,googl,fb):

        self.assertEqual(google.call_google_api(),'data_2')
        self.assertEqual(facebook.call_facebook_api(),'data_3')

class TestApiSecond(TestCase):
    """
    Testing with differnet side_effects
    """
    @mock.patch('google.get_data',side_effect =["data_4","data_5","data_6"])
    def test_external_api(self,googl):
        self.assertEqual(google.call_google_api(), 'data_4')
        self.assertEqual(google.call_google_api(), 'data_5')
        self.assertEqual(google.call_google_api(), 'data_6')


class TestApiThird(TestCase):
    """
    Testing with differnet side_effects exceptions
    """
    @mock.patch('google.get_data',side_effect =Exception('Boom'))
    def test_external_api(self,googl):
        self.assertRaises(Exception,googl)


class TestApiFourth(TestCase):
    """
    Testing with differnet side_effects exceptions but with mock patch object
    """
    @mock.patch.object(google,'get_data',side_effect =Exception('Boom'))
    def test_external_api(self,googl):
        self.assertRaises(Exception,googl)