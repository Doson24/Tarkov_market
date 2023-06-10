import datetime
import os
import pandas as pd
from collections import OrderedDict


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

while True:
    name = input('Введите название предмета: ')
    pr = df[df.Name == name]
    #df.ц
    # pr = pr.sort_values('Date')
    print(pr[['avg_price_24h', 'price_sell_trader', 'name_trader']])