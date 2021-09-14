import unittest
from app.models import NewsArticle

class NewsArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = NewsArticle('Thriling api news. Watchout!')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,NewsArticle))

    if __name__ == '__main__':
        unittest.main()
