def sum_ints_div_by_either_nums(numbers):
    start, end = (299, 382)
    total_sum = sum((num for num in numbers[start:end + 1] if num % 858 == 0 or num % 952 == 0))
    return total_sum