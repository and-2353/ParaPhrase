# coding:utf-8
import os
import csv
import requests
import re
import os
import sqlite3
from tqdm import tqdm
from janome.tokenizer import Tokenizer
from pprint import pprint
import pickle
import random
import gensim

# htmlからのデータをcsvファイルに記録
def write_csv(data):
    datas = [data]
    with open(os.getcwd()+'/app/application/'+'data.csv','a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(datas)


def return_text():
    return 'Hello'


def convert_data(data):
    datas = [data]
    return "!!"+ str(datas) + "??"


def open_synonims():
    """
    synonims を開く
    """
    with open('objects/synonims.pickle', mode='rb') as p:
        synonims = pickle.load(p)
    return synonims


def get_synonims(model, word):
    return model.most_similar(word, topn=1)[0][0]


def paraphrase(data):
    datas = [data]

    t = Tokenizer()
    model = gensim.models.Word2Vec.load(os.getcwd()+'/app/application/'+'data/ja.bin')

    text = ""

    for token in t.tokenize(datas[0]):
        pos = token.part_of_speech.split(',')[0]
        if pos == '名詞':
            try:
                text += get_synonims(model, token.base_form)
            except KeyError:
                text += token.base_form
        else:
            text += token.surface
    return text
        