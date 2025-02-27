def lists_with_product_equal_n(lst):
    n = -41
    result = []
    n_elements = len(lst)
    for i in range(n_elements):
        product = 1
        for j in range(i, i + n_elements):
            product *= lst[j % n_elements]
            if product == n:
                result.append(lst[i:j % n_elements + 1])
    return result