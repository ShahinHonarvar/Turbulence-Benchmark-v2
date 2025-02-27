def sum_ints_div_by_either_nums(numbers):
    """
    <Write a function called'sum_ints_div_by_either_nums' that takes one argument, a list of integers, and returns the sum of all integers divisible by either 56 or 68 from index 81 to index 89, both inclusive. If no such integers exist in the specified range, the function should return 0.>
    """
    return sum((n for i, n in enumerate(numbers) if i >= 81 and i <= 89 and (n % 56 == 0) or n % 68 == 0))