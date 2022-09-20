test_1 = 3
test_2 = 2

def pangkat(pangkat, angka):
    sum = 1
    while angka:
        if angka & 1:
            sum *= pangkat
        pangkat *= pangkat
        angka >>= 1
    return sum

print(pangkat(test_1, test_2))