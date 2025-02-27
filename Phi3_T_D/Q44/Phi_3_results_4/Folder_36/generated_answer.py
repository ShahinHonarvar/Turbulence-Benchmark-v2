def is_composite(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

def composite_nums_between_indices(numbers):
    return {n for n in numbers[686:988] if is_composite(n)}