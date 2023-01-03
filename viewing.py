import datetime
import os
from collections import OrderedDict
import pandas as pd


def search_files(path: str) -> list:
    """
    Поиск всех .xls файлов в папке

    :param path:
    :return:
    """

    list_dir = os.listdir(path)
    list_files = [i for i in list_dir if '.csv' in i]
    return list_files


filenames = search_files('data')

# При парсинге путает день и месяц
dict_of_df = OrderedDict(('data/'+f, pd.read_csv('data/'+f, parse_dates=['Date'])) for f in filenames)

df = pd.concat(dict_of_df, sort=True)
pr = df[df.Name == 'Ключ от номера 220 западного крыла Санатория']
pr = pr.sort_values('Date')

print(pr.avg_price_24h)