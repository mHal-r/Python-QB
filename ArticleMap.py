class ArticleMap(object):
    article_words = set()
    article_num = set()
    def _init_ (self, words, numbers):
        self.article_words = words
        self.article_num