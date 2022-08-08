from collections import OrderedDict
import pandas as pd


filenames = ['data12-07-2022.csv', 'data13-07-2022.csv', 'data28-07-2022.csv', 'data08-08-2022.csv']
dict_of_df = OrderedDict((f, pd.read_csv(f)) for f in filenames)
df = pd.concat(dict_of_df, sort=True)
# df = pd.read_csv('data08-08-2022.csv')
pr = df[df.Name == 'Сошки для HK G36'].price_sell_trader
print(pr)