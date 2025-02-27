def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    target_product = 632
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= lst[index]
            if product == target_product:
                result.append(lst[start:index + 1])
            elif product > target_product:
                break
    return result