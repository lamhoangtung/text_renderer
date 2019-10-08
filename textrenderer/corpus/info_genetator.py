from textrenderer.corpus.corpus import Corpus
import json
import os
import random

import numpy as np
import pandas as pd
from PIL import Image

from data.info.dantoc import dan_toc_db
from data.info.dihinh import *
# For name generation
from data.info.fake_name_db import family_names, first_names, middle_names
from data.info.tongiao import ton_giao_db

real_name_db = [each['full_name']
                for each in json.loads(open('./data/info/real_name.json', 'r').read())]

# For address generation
address_db = pd.read_csv('./data/info/address.csv')
tinh_tp = pd.unique(address_db['Tỉnh Thành Phố'])
quan_huyen = pd.unique(address_db['Quận Huyện'])
phuong_xa = pd.unique(address_db['Phường Xã'])

# For profiles images generation

def get_rand_name(is_can_cuoc=False):
    name = ''
    fake_name = random.uniform(0, 1) < 0.2
    if fake_name:
        if random.uniform(0, 1) <= 0.4:
            name = '{} {} {} {}'.format(random.choice(family_names), random.choice(
                middle_names), random.choice(middle_names), random.choice(first_names))
        else:
            name = '{} {} {}'.format(random.choice(family_names), random.choice(
                middle_names), random.choice(first_names))
    else:
        name = random.choice(real_name_db)
    if random.uniform(0, 1) <= 0.7 or is_can_cuoc:
        return name.upper()
    else:
        return name


def get_rand_dob(is_can_cuoc=False):
    if is_can_cuoc:
        return '{:02d}/{:02d}/{:04d}'.format(random.randint(1, 31), random.randint(1, 12), random.randint(1850, 2100))
    else:
        return '{:02d}-{:02d}-{:04d}'.format(random.randint(1, 31), random.randint(1, 12), random.randint(1850, 2100))


def get_rand_id(is_can_cuoc=False):
    if is_can_cuoc:
        id = '{:12d}'.format(random.randint(1, 999999999999))
    else:
        id = '{:09d}'.format(random.randint(1, 999999999))
    return ' '.join([each for each in id])


def get_rand_nguyen_quan():
    have_prefix = True if random.uniform(0, 1) <= 0.35 else False
    address = address_db.sample(n=1, random_state=np.random.RandomState())

    address = '{}, {}, {}'.format(
        address['Phường Xã'].values[0], address['Quận Huyện'].values[0], address['Tỉnh Thành Phố'].values[0])
    # print(address)
    # import ipdb; ipdb.set_trace()
    if not have_prefix:
        address = address.replace('Tỉnh ', '').replace('Thành phố ', '').replace('Quận ', '').replace(
            'Huyện ', '').replace('Xã ', '').replace('Phường ', '').replace('Thị trấn ', '').replace('Thị xã ', '')
    else:
        short_case = {
            'Thị xã ': 'Tx.',
            'Quận ': 'Q.',
            'Thị trấn ': 'Tt.',
            'Thành phố ': 'TP.',
            'Huyện ': 'H.',
            'Phường ': 'P.',
            'Tỉnh ': 'T.'
        }
        for each in short_case:
            if random.uniform(0, 1) <= 0.85:
                address = address.replace(each, short_case[each])
    return address, have_prefix


def get_rand_address(base_address, have_prefix):
    have_address_number = random.randint(0, 2)

    if have_address_number > 0:
        address_number = '/'.join([str(random.randint(1, 1000))
                                   for _ in range(have_address_number)])
        if have_prefix:
            address_number = '{} {}'.format(random.choice(
                ['Số', 'Số nhà', 'Lô', 'Ấp']), address_number)
    else:
        address_number = ""

    street = random.choice(phuong_xa)
    if not have_prefix:
        street = street.replace('Xã ', '').replace(
            'Phường ', '').replace('Thị trấn ', '').replace('Thị xã ', '')
    else:
        street = street.replace('Xã ', 'Đường ').replace(
            'Phường ', 'Đường ').replace('Thị trấn ', 'Đường ').replace('Thị xã ', 'Đường ')

    if have_address_number > 0:
        return '{}, {}, {}'.format(address_number, street, base_address)
    else:
        return '{}, {}'.format(street, base_address)


# For random dan toc generation


def get_rand_dan_toc():
    return random.choice(dan_toc_db)


# For random ton giao generation


def get_rand_ton_giao():
    return random.choice(ton_giao_db)


def get_rand_noi_cap():
    address = random.choice(tinh_tp)
    if random.uniform(0, 1) <= 0.5:
        short_case = {
            'Thành phố ': 'TP.',
            'Tỉnh ': 'T.'
        }
        for each in short_case:
            address = address.replace(each, short_case[each])
    return address


def get_rand_ngay_cap():
    day = get_rand_dob().split('-')
    return {
        'ngay_cap': day[0],
        'thang_cap': day[1],
        'nam_cap': day[2]
    }


def get_rand_di_hinh():
    res = random.choice(loai_di_hinh)
    if random.uniform(0, 1) <= 0.85:
        res += ' {} {:.2f} cm'.format(random.choice(
            tu_noi_khoang_cach), random.uniform(0.2, 2.5))
    res += ' '
    res += random.choice(vi_tri)
    res += ' '
    res += random.choice(tu_noi_khoang_cach)
    res += ' '
    res += random.choice(tu_noi_vi_tri)
    return res


def get_rand_gender():
    return random.choice(['Nam', 'Nữ'])


def get_rand_nationality():
    return random.choice(['Việt Nam'])


# For random string generation
corpus = open('./data/info/news_corpus.txt', 'r').read()
# corpus = open('./data/corpus-full.txt', 'r').read()
# corpus = corpus.replace('\n', ' ')
sentences = corpus.split('\n')

words = []
for each in sentences:
    words.extend(each.split(' '))
words = list(set(words))
words = list(filter(lambda x: len(x) <= 11, words))
avg_len = np.mean([len(each) for each in words])


def sample_from_corpus(max_length=70):
    num_words = random.randint(3, int(max_length/avg_len)-1)
    candidates = random.sample(words, num_words)
    text = ' '.join(candidates)
    while len(text) > max_length:
        candidates = random.sample(words, num_words)
        text = ' '.join(candidates)
    return text


def get_random_info_front(is_can_cuoc=False, ocr_only=False):
    nguyen_quan, have_prefix = get_rand_nguyen_quan()
    info = {
        "id": get_rand_id(is_can_cuoc),
        "ho_ten": get_rand_name(is_can_cuoc),
        "ngay_sinh": get_rand_dob(is_can_cuoc),
        "nguyen_quan": nguyen_quan,
        "ho_khau_thuong_tru": get_rand_address(nguyen_quan, have_prefix)
    }
    if is_can_cuoc:
        info["gioi_tinh"] = get_rand_gender()
        info["quoc_tich"] = get_rand_nationality()
        info["ngay_het_han"] = get_rand_dob(is_can_cuoc)
    # if ocr_only and random.uniform(0, 1) < 0.15:
    #     info["nguyen_quan"] = sample_from_corpus(max_length=60)
    #     info["ho_khau_thuong_tru"] = sample_from_corpus(max_length=70)
    return info


def get_random_info_back(is_can_cuoc=False, ocr_only=False):
    d1 = {
        "dau_vet": get_rand_di_hinh(),
    }
    if ocr_only and random.uniform(0, 1) < 0.5:
        d1["dau_vet"] = sample_from_corpus(max_length=80)
    if not is_can_cuoc:
        d1["dan_toc"] = get_rand_dan_toc()
        d1["ton_giao"] = get_rand_ton_giao()
        d1["noi_cap"] = get_rand_noi_cap()
    d2 = get_rand_ngay_cap()
    return dict(d1, **d2)

def create_random_corpus():
    # info1 = get_random_info_front(is_can_cuoc=random.uniform(0, 1) >= 0.5)
    # info2 = get_random_info_back(is_can_cuoc=random.uniform(0, 1) >= 0.5)
    # info1['id'] = info1['id'].replace(' ','')
    # text = list(info1.values()) + list(info2.values())
    # return random.choice(text)
    return get_rand_id().replace(' ','')

class IDCorpus(Corpus):
    def load(self):
        pass

    def get_sample(self, img_index):
        return create_random_corpus()

if __name__ == "__main__":
    # for _ in range(100):
    #     print(get_random_info_front(is_can_cuoc=True))
    #     print('-------------------')
    #     print(get_random_info_back(is_can_cuoc=True))
    #     print('===================')
    create_random_corpus()
