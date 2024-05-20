# report.py
#
# Exercise 2.4
import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f).split(',')
        for row in rows:
            holding = dict(zip(headers, row))
            # holding = {
            #     "name":row[0],
            #     "price":float(row[2]),
            #     "shares": int(row[1])
            # }
            print(holding)
            portfolio.append(holding)
        return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = row[1]
            except:
                continue
        return prices

def compute(portfolio, prices):
    # current value and the loss or gain
    final=[]
    for row_dict in portfolio:
        new_price = float(prices[row_dict["name"]])
        old_price = float(row_dict["price\n"])
        shares = row_dict["shares"]
        name = row_dict["name"]
        result = {
            "name": name,
            "shares": shares,
            "price": new_price,
            "change": new_price - old_price
        }
        final.append(result)
    return final

def make_report(portfolio, prices):
    final_tuple = []
    for row_dict in portfolio:
        new_price = float(prices[row_dict["name"]])
        old_price = float(row_dict["price\n"])
        shares = row_dict["shares"]
        name = row_dict["name"]
        change = new_price - old_price
        stock_tple = (name, shares, new_price, change)
        final_tuple.append(stock_tple)
    return final_tuple

def fmt_report(report):
    print(f'{"Name":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
    print(f'---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        cnt= str(price)
        fmt = 10-len(cnt)
        print(f'{name:>10s} {shares:>10s} {"$":>{fmt}s}{price:0.2f} {change:>10.2f}')

portfolio = read_portfolio('/Users/florinamary/Documents/practical-python/Work/Data/portfolio.csv')
# print(portfolio)

prices = read_prices('/Users/florinamary/Documents/practical-python/Work/Data/prices.csv')
# print(prices)

computed = compute(portfolio, prices)
# print(computed)

report = make_report(portfolio, prices)
# print(report)

fmt_report(report)
