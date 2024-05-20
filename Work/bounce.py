# bounce.py
#
# Exercise 1.5

bounces = 10
height = 100
for bounce in range(0, bounces):
    height = round(height * (3/5),4)
    print(bounce+1, height)
