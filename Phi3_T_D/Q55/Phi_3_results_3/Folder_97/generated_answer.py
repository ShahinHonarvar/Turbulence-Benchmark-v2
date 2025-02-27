def lists_with_product_equal_n(circular_list):
    n = -938
    results = []
    length = len(circular_list)
    circular_list += circular_list[:-1]
    for i in range(length):
        product = 1
        for j in range(i, length * 2):
            product *= circular_list[j % length]
            if product == n:
                results.append(circular_list[i:j + 1])
            elif product > n:
                break
    return results