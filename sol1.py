print("Solution 1")
def find_sum():
    s = 0
    for i in range(1,1000): 
        if (i%3 == 0) or (i%5 == 0):
            s += i
    print("The sum of multiple of 3 & 5 below 1000 is",s)

find_sum()
