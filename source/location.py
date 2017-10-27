from pprint import pprint

import nltk
from nltk.tag.stanford import StanfordNERTagger

from source.constants import absolutify


class MetaStanford(type):
    def __init__(cls, name, bases, d):
        type.__init__(cls, name, bases, d)
        import os
        os.environ['CLASSPATH'] = absolutify('stanford-ner.jar')


class NERTagger(metaclass=MetaStanford):
    def __init__(self, model=None):
        self.tagger = StanfordNERTagger(model or absolutify('models', 'english.all.3class.distsim.crf.ser.gz'))

    def tag_sentence(self, sent):
        return self.tagger.tag(nltk.word_tokenize(sent))


tagger = NERTagger()
pprint(tagger.tag_sentence("Rami Eid is studying at Stony Brook University in NY"))
