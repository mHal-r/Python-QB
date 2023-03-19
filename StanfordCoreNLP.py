
from pycorenlp import StanfordCoreNLP
import logging
import json

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,pos,lemma,depparse,natlog,openie',
            'pipelineLanguage': 'en',
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return self.nlp.annotate(sentence, properties=self.props)

    # @staticmethod
    # def tokens_to_dict(_tokens):
    #     tokens = defaultdict(dict)
    #     for token in _tokens:
    #         tokens[int(token['index'])] = {
    #             'word': token['word'],
    #             'lemma': token['lemma'],
    #             'pos': token['pos'],
    #             'ner': token['ner']
    #         }
    #     return tokens