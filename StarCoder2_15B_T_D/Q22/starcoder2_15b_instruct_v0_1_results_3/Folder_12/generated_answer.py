def find_sum_of_multiples(num: int) -> int:
    total = 0
    for i in range(1, 86):
        multiple = num * i
        total += multiple
    return total