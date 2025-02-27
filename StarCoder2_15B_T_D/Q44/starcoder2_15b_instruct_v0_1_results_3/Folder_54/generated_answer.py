def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composite_nums = set()
    for i, n in enumerate(lst):
        if is_composite(n) and 14 <= i <= 64:
            composite_nums.add(n)
    return composite_nums