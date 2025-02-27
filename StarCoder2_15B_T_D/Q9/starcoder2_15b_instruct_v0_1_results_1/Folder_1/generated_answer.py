def all_odd_ints_inclusive(numbers):
    return [x for i, x in enumerate(numbers) if i >= 31 and i <= 72 and (x % 2 == 1)]