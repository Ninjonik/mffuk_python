def gcd(x, y):
    while x > y:
        if y > x:
            x, y = y, x
        else:
            x = x % y
    return x

print(gcd(27,21))