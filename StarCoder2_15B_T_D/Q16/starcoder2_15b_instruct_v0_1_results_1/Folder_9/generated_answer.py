def sum_even_ints_inclusive(numbers):
    """
    <Write a function called'sum_even_ints_inclusive' that takes one argument, a list of integers, and returns the sum of all even integers from index 70 to index 200, both inclusive. If no even integers exist in the specified range, the function should return 0.>
    """
    sum = 0
    for i in range(70, 201):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum