def lists_with_product_equal_n(circular_list):
    """
    Find all sublists of a circular list where the product of elements equals -91.

    Args:
    circular_list (list): Circular list of integers.

    Returns:
    list: List containing all sublists that meet the criteria.
    """
    result = []
    n = len(circular_list)
    for i in range(n):
        for m in range(i + 1, n + i + 1):
            sublist = circular_list[i:m % n]
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                result.append(sublist)
    return result