import itertools

def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals -94.
    """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and len(sublist) > 0 and (len(sublist) < 10) and (product(sublist) == -94):
                sublists.append(sublist)
    return sublists

def product(numbers):
    """
    Returns the product of a list of numbers.
    """
    result = 1
    for number in numbers:
        result *= number
    return result