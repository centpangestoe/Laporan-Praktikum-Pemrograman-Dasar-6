def max_bilangan(a, b, c, d):
    maks = a
    for x in (b, c, d):
        if x > maks:
            maks = x
    return maks

a, b, c, d = map(int, input().split())
print(max_bilangan(a, b, c, d))