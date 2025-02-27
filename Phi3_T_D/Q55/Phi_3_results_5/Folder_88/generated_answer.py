def lists_with_product_equal_n(circular_list):
    n = -56
    results = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            if j - i >= 2:
                product = 1
                for k in range(i, j):
                    product *= circular_list[k % len(circular_list)]
                    if product == n:
                        results.append(circular_list[i % len(circular_list):j % len(circular_list)])
                        break
                    elif product > n:
                        break
    return results