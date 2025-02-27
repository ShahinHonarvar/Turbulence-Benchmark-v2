def sum_in_range(numbers):
    return sum((x for x in numbers if 142 <= x <= 407)) if any((142 <= x <= 407 for x in numbers)) else 0