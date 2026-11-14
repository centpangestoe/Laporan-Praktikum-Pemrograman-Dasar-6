def maksimal(a, b):
    return a if a > b else b

def minimal(a, b):
    return a if a < b else b

n = int(input())
maks = -100000
minim = 100000

nilai_list = input().split()
for i in range(n):
    nilai = int(nilai_list[i])
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)

print(maks, minim)