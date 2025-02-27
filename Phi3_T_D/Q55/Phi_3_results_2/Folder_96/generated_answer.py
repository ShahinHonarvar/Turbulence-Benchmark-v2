def lists_with_product_equal_n(lst):
    circular_len = len(lst)
    result = []
    for i in range(circular_len):
        product = 1
        for j in range(i, i + circular_len):
            product *= lst[j % circular_len]
            if product == 0:
                result.append(lst[i:j + 1])
    return result