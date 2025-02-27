def if_perfect_num(numbers):
    sums = [sum((1 for i in range(1, n // 2 + 1) if n % i == 0)) for n in numbers]
    return sums[0] == numbers[0]