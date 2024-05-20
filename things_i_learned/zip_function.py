columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)

# A common use of zip is to create key/value pairs for constructing dictionaries.
d = dict(zip(columns, values))

# Inverting a dictionary

prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }

# If you use the items() method, you can get (key,value) pairs:
# However, what if you wanted to get a list of (value, key) pairs instead? Hint: use zip().

pricelist = list(zip(prices.values(),prices.keys()))
min(pricelist)
max(pricelist)
sum(pricelist)

sorted(pricelist)
