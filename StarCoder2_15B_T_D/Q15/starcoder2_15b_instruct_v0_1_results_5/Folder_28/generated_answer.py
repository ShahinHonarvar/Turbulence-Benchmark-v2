def sum_odd_ints_inclusive(lst):
    """
    <Write a function called'sum_odd_ints_inclusive' that takes one argument, a list of integers, and returns the sum of all odd integers from index 62 to index 63, both inclusive. If no odd integers exist in the specified range, the function should return 0.>
    """
    sum = 0
    for i in range(62, 64):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum