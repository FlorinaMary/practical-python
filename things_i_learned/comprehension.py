# dictionary comprehension is possible in python
names = { name: 0 for name in names }
for s in portfolio:
    holdings[s['name']] += s['shares']

# holdings{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }

#  Comprehension summary
import csv
f = open('Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
# ['name', 'date', 'time', 'shares', 'price']

select = ['name', 'shares', 'price']

indices = [ headers.index(colname) for colname in select ]
row = next(rows)

record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
# {'price': '32.20', 'name': 'AA', 'shares': '100'}

portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
'''
[{'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'},
  {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'},
  {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
'''
