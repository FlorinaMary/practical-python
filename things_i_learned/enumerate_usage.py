'''
Sometimes the for statement, len(), and range() 
get used by novices in some kind of horrible code fragment that looks like it emerged from the depths of a rusty C program.

Don’t do that! Not only does reading it make everyone’s eyes bleed, it’s inefficient with memory and it runs a lot slower. 
Just use a normal for loop if you want to iterate over data. Use enumerate() if you happen to need the index for some reason.
'''

names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Loops with i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'

    pass

with open(filename="") as f:
    for lineno, line in enumerate(f, start=1):
        ...
        pass

