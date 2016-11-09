print("Solution 2")
def sol2(n):
    a,b = 1,1
    c = 0
    for i in range(n):
        a,b = b,a+b
        if(a%2 == 0):
            c += a
        if (c >= 4000000):
            break
    return c
    
print(sol2(40))