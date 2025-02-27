def sum_even_ints_inclusive(numbers):
    if len(numbers) < 81:
        return 0
    return sum((x for x in numbers[8:81] if x % 2 == 0))