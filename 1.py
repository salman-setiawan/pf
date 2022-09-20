test = [1, 2, 3]

def square(n):
    return n * n

def sum_squares(n_list):
    return sum(list(map(square, n_list)))

print(sum_squares(test))