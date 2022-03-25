import pandas as pd
import numpy as np
f = open('/home/catmas/Documents/Python/STP/src/test/stock_basic.csv', 'r')
df = pd.read_csv(
    '/home/catmas/Documents/Python/STP/src/test/stock_basic.csv', encoding='utf-8')
# data_1 = df.loc[:['code']]
df[['code']].to_csv(
    '/home/catmas/Documents/Python/STP/src/test/new_stock_basic.csv',
    encoding='utf_8_sig', index=None)
# print(data_1.to_string())
f.close
