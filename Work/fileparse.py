# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        records = []
        # Read the file headers
        if has_headers:
            headers = next(rows)
            sel_headers = []
            if select:
                sel_headers = [headers.index(sel) for sel in select]
            else:
                sel_headers=[]

            headers = select
            for row in rows:
                if types:
                    row = [types[ind](row[ind]) for ind in sel_headers]
                else:
                    row = [row[ind] for ind in sel_headers]
                if not row:    # Skip rows with no data
                    continue
                
                record = dict(zip(headers, row))
                records.append(record)
        else:
            for row in rows:
                record = tuple(row)
                records.append(record)

    return records

# portfolio = parse_csv('Work/Data/portfolio.csv')
portfolio = parse_csv('Work/Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
# print(portfolio)

prices = parse_csv('Work/Data/prices.csv', types=[str,float], has_headers=False)
print(prices)