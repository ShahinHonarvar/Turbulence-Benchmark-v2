def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    result = set()
    for i, n in enumerate(lst):
        if is_composite(n) and 27 <= i <= 55:
            result.add(n)
    return result