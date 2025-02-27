def if_perfect_num(numbers):
    if 47 >= len(numbers):
        return False
    n = numbers[47]
    return n == sum((x for x in range(1, n) if n % x == 0))