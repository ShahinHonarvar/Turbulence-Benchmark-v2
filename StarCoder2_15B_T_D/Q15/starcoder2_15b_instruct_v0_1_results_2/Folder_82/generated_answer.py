from index 20 to index 200, both inclusive. If no odd integers exist in the

def sum_odd_ints_inclusive(numbers):
    """
    This function takes a list of integers and returns the sum of all odd integers
    specified range, the function returns 0.
    """
    sum_odd = 0
    for i, num in enumerate(numbers):
        if i >= 20 and i <= 200 and (num % 2 != 0):
            sum_odd += num
    return sum_odd