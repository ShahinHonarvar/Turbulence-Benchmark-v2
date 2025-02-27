def lists_with_product_equal_n(circular_list):
    n = 990
    result = []
    nlen = len(circular_list)
    if nlen == 0:
        return result
    for start in range(nlen):
        product = 1
        for length in range(1, nlen + 1):
            index = (start + length - 1) % nlen
            product *= circular_list[index]
            if product == n:
                result.append(circular_list[start:start + length])
            elif product > n:
                break
    return result