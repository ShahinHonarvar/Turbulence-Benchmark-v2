def find_sum_of_multiples(num):
    return sum((i for i in range(1, 256) for j in range(1, num + 1) if i * j == num))