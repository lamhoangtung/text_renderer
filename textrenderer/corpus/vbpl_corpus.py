from textrenderer.corpus.corpus import Corpus

class VBPLCorpus(Corpus):
    def load(self):
        self.all_lines = open('data/corpus/extracted_300k.txt','r').read().split('\n')

    def get_sample(self, index):
        return self.all_lines[index]
