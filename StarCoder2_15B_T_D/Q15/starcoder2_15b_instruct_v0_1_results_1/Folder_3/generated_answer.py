def sum_odd_ints_inclusive(numbers):
    if len(numbers) >= 93:
        odd_ints = [n for n in numbers[62:93] if n % 2 == 1]
        if len(odd_ints) > 0:
            return sum(odd_ints)
    return 0