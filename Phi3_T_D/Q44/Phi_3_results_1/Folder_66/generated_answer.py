def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    if len(numbers) < 64:
        return set()
    return {numbers[i] for i in range(62, 64) if is_composite(numbers[i])}