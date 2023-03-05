# python3 -m pip install pandas

import pandas

address = pandas.read_csv('address.csv')

print(address)
print(address.head(2))
print(address.describe()) # 요약