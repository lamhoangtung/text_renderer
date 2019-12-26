from textrenderer.corpus.corpus import Corpus
from textrenderer.corpus.info_genetator import get_random_info_front, get_random_info_back
import random
import numpy as np

key_to_string = {
    'id': ["Số"],
    'ho_ten': ['Họ và tên', 'Họ tên'],
    'ngay_sinh': ['Ngày sinh', 'Ngày tháng năm sinh', 'Sinh'],
    'nguyen_quan': ['Nguyên quán', 'Quê quán'],
    "ho_khau_thuong_tru": ['Hộ khẩu thường trú', 'Nơi thường trú'],
    'gioi_tinh': ['Giới tính'],
    'quoc_tich': ['Quốc tịch'],
    'ngay_het_han': ['Ngày hết hạn', 'Hạn đến'],
    'dau_vet': ['Dị hình', 'Dấu vết nhận diện', 'Đặc điểm nhận dạng', 'Dấu vết riêng và dị hình'],
    'dan_toc': ['Dân tộc'],
    'ton_giao': ['Tôn giáo'],
    'noi_cap': ['Giám đốc CA']
}


class CMNDCorpus(Corpus):
    def load(self):
        pass

    def get_sample(self, index):
        cc = random.randint(0, 1)
        front = random.randint(0, 1)
        long = random.randint(0, 3)
        # print('getting')
        if cc:
            if front:
                data = get_random_info_front(is_can_cuoc=True, ocr_only=True)
            else:
                data = get_random_info_back(is_can_cuoc=True, ocr_only=True)
        else:
            if front:
                data = get_random_info_front(ocr_only=True)
            else:
                data = get_random_info_back(ocr_only=True)
        # print('done')
        picked_key = random.choice(list(data.keys()))
        # print(picked_key)
        text = data[picked_key]
        # print(text)
        if long >= 1:
            if picked_key in ['ngay_cap', 'thang_cap', 'nam_cap']:
                if random.randint(0, 1) == 0:
                    text = 'ngày {} tháng {} năm {}'.format(
                        data['ngay_cap'], data['thang_cap'], data['nam_cap'])
                else:
                    text = '{}/{}/{}'.format(data['ngay_cap'], data['thang_cap'], data['nam_cap'])
            else:
                text = random.choice(key_to_string[picked_key]) + ': ' + text
        words = text.split(' ')
        for index, word in enumerate(words):
            # 0: lowercase, 1: firstupcase, 2: allupcase
            mode = int(np.random.choice(3, 1, p=[0.65, 0.25, 0.1]))
            if mode == 1:
                words[index] = word.title()
            elif mode == 2:
                words[index] = word.upper()
        text = ' '.join(words)
        return text
