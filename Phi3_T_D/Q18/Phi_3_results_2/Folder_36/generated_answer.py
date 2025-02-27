def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[299:383 + 1], start=299) if num % 858 == 0 or num % 952 == 0))