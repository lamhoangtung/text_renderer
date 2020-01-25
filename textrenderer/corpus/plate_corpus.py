import random
import rstr
from textrenderer.corpus.corpus import Corpus

seri_db = {
    'quan_su': ['AA', 'AB', 'AC', 'AD', 'AV', 'AT', 'AN', 'AP', 'BBB', 'BC', 'BH', 'BK', 'BL', 'BT', 'BP', 'BS', 'BV', 'HA', 'HB', 'HC', 'HD', 'HE', 'HT', 'HQ', 'HN', 'HH', 'KA', 'KB', 'KC', 'KD', 'KV', 'KP', 'KK', 'KT', 'KN', 'PA', 'PP', 'PM', 'PK', 'PT', 'PY', 'PQ', 'PX', 'PC', 'QA', 'QB', 'QH', 'TC', 'TH', 'TK', 'TT', 'TM', 'TN', 'DB', 'ND', 'CH', 'VB', 'VK', 'CV', 'CA', 'CP', 'CM', 'CC', 'VT', 'CB', 'AX', 'HL'], # red,
    'nuoc_ngoai': ['NG', 'QT', 'CV', 'NN'],
    'dac_biet': ['KT', 'LD', 'DA', 'R', 'T', 'MK', 'MĐ', 'TĐ', 'HC']
}


class PlateCorpus(Corpus):
    """
    Generate bien so corpus
    """

    def load(self):
        pass

    def random_length_n(self, n):
        return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])

    def get_sample(self, img_index):
        plate_type = random.randint(1, 5)
        # print(plate_type)
        if plate_type == 4: # xe quan su
            seri = random.choice(seri_db['quan_su'])
            text = '{} {}-{}'.format(seri, self.random_length_n(2), self.random_length_n(2))
        elif plate_type in [1, 2]: # bien thong thuong, xanh
            province_code = random.randint(11, 99)
            seri = rstr.xeger(r'[A-Z][A-Z0-9]') if random.randint(0, 1) == 0 else random.choice(seri_db['dac_biet'])
            if random.randint(0, 1) == 0:
                text = '{}-{} {}.{}'.format(province_code, seri, self.random_length_n(3), self.random_length_n(2))
            else:
                text = '{}{} {}.{}'.format(province_code, seri, self.random_length_n(3), self.random_length_n(2))
        elif plate_type == 3: # vang (xe kinh te)
            province_code = random.randint(11, 99)
            text = '{}{} {}.{}'.format(province_code, rstr.xeger(r'[A-Z][A-Z]'), self.random_length_n(3), self.random_length_n(2))
        elif plate_type == 5: # xe nuoc ngoai
            province_code = random.randint(11, 99)
            seri = random.choice(seri_db['nuoc_ngoai'])
            if random.randint(0, 1) == 0:
                text = '{}-{} {}.{}'.format(province_code, seri, self.random_length_n(3), self.random_length_n(2))
            else:
                text = '{}{} {}.{}'.format(province_code, seri, self.random_length_n(3), self.random_length_n(2))
        # text = text.replace('D', 'Đ')
        # text = '21-Đ1 972.78'
        return text

if __name__ == "__main__":
    corpus = PlateCorpus('data/chars/plate.txt')
    for _ in range(100):
        print(corpus.get_sample(1))
