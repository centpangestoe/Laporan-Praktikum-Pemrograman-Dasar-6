def mutlak(angka):
    return -angka if angka < 0 else angka

def hitung(nilai1, nilai2):
    return mutlak(nilai1 - nilai2)

x1, y1, x2, y2 = map(int, input().split())
print(mutlak(hitung(x1, x2) + hitung(y1, y2)))