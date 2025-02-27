def sum_of_divisors_in_range(n):
    """
    You are given a text specification surrounded by angle brackets.
    Create Python code according to the text specification.
    The Python code should not contain any comments.
    The Python code should be delimited only by triple backticks.
    Write a function called'sum_of_divisors_in_range' that takes a positive integer as its argument,
    and returns the sum of all positive divisors of the given integer that are between 11 and 56, both inclusive.
    If no such divisors exist in the specified range, the function should return 0.
    """
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and 11 <= i <= 56:
            sum += i
    return sum