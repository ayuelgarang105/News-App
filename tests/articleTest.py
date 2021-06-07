from app.models import Article
class ArticlesTest:
    '''
    method to test articles
    '''

    def setUp(self):
        self.new_article = Article(123,'world', 'hello','nourl','url')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article))