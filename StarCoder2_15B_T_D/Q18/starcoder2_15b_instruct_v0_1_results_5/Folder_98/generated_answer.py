def sum_ints_div_by_either_nums(numbers):
    """
    Returns the sum of all integers divisible by either -1 or 13 from index 0 to index 5, both inclusive.
    If no such integers exist, returns 0.
    """
    sum_divisible = 0
    for i in range(6):
        if numbers[i] % -1 == 0 or numbers[i] % 13 == 0:
            sum_divisible += numbers[i]
    return sum_divisible