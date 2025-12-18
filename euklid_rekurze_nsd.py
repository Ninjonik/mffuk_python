def euklid(x, y):
    if x % y == 0:
        return y

    return euklid(y, x % y)

print(euklid(897897, 34984894))