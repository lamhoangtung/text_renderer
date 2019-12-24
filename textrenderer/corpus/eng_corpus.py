from textrenderer.corpus.corpus import Corpus
import numpy as np
import random

class EngCorpus(Corpus):
    """
    Load English corpus by words, and get random {self.length} words as result
    """

    def load(self):
        self.load_corpus_path()

        for i, p in enumerate(self.corpus_path):
            print("Load {} th eng corpus".format(i))
            with open(p, encoding='utf-8') as f:
                data = f.read()

            lines = data.split('\n')
            for line in lines:
                for word in line.split(' '):
                    word = word.strip()
                    word = ''.join(filter(lambda x: x in self.charsets, word))

                    if word != u'' and len(word) > 2:
                        self.corpus.append(word)
            print("Word count {}".format(len(self.corpus)))

    def get_sample(self, img_index):
        # start = np.random.randint(0, len(self.corpus) - self.length)
        # words = self.corpus[start:start + self.length]
        words = random.sample(self.corpus, k=random.randint(2, self.length))
        for index, word in enumerate(words):
            mode = int(np.random.choice(3, 1, p=[0.65, 0.25, 0.1])) # 0: lowercase, 1: firstupcase, 2: allupcase
            if mode == 1:
                words[index] = word.title()
            elif mode == 2:
                words[index] = word.upper()
        word = ' '.join(words)
        return word
