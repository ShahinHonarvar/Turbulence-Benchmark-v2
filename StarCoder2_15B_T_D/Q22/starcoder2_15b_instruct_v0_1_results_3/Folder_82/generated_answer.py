def find_sum_of_multiples(num):
    """
    Write a function called 'find_sum_of_multiples' that takes one argument, a positive integer,
    and returns the sum of the first 33 possitive multiples of the given integer.
    """
    return sum((num * i for i in range(1, 34)))