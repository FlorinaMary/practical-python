# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    with open(filename, "rt") as f:
        total_cost = 0
        headers=next(f).split(',')
        for rowno, row in enumerate(f, start=1):
            row = row.split(',')
            record = dict(zip(headers, row))
            print(record)
            try:
                nshares = int(record['shares'])
                price = float(record['price\n'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        return total_cost

def throw(filename):
    with open(filename, 'rt') as f:
        next(f)
        for lineno, line in enumerate(f, start=1):
            try:
                data = line.split(',')
                shares = int(data[1])
                price = float(data[2])
            except:
                print(f"Row {lineno} Couldn't convert: {data}")


cost = portfolio_cost('Work/Data/portfolio.csv')
print('Total cost:', cost)

# new_cost = portfolio_cost('Work/Data/portfoliodate.csv')
# print('Total cost:', new_cost)

# throw('Work/Data/missing.csv')