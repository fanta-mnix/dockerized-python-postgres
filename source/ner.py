from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer

from source.constants import absolutify


class MetaStanford(type):
    def __init__(cls, name, bases, d):
        type.__init__(cls, name, bases, d)
        import os
        os.environ['CLASSPATH'] = ':'.join([absolutify('stanford-postagger.jar'), absolutify('stanford-ner.jar')])
        os.environ['STANFORD_MODELS'] = ':'.join([
                absolutify('models', 'english-left3words-distsim.tagger'),
                absolutify('models', 'english.all.3class.distsim.crf.ser.gz')])


class NERTagger(metaclass=MetaStanford):
    def __init__(self):
        self._tokenizer = StanfordTokenizer()
        self._tagger = StanfordNERTagger(absolutify('models', 'english.all.3class.distsim.crf.ser.gz'))

    def tag_sentence(self, sent):
        return self._tagger.tag(self._tokenizer.tokenize(sent))

