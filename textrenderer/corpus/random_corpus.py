import random

from textrenderer.corpus.corpus import Corpus


class RandomCorpus(Corpus):
    """
    Load charsets and generate random word line from charsets
    """

    def load(self):
        pass

    def get_sample(self, img_index):
        # word = ''
        # for _ in range(self.length):
        #     word += random.choice(self.charsets)
        # return word

        num_words = random.randint(3, 20)
        text = []
        for _ in range(num_words):
            word = ''
            num_chars = random.randint(1, 9)
            for _ in range(num_chars):
                word += random.choice(self.charsets)
            text.append(word)
        text = ' '.join(text)
        # print(text)
        return text

