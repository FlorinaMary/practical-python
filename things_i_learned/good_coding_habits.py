# Prefer keyword arguments in function calls

def parse_data(data):
    pass


data = ""
parse_data(data, False, True) # ?????

# optional arguments will come after the required arguments.
parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)

# Modifying global variables

name = 'Dave'

def spam():
    global name
    name = 'Guido' # Changes the global name above
