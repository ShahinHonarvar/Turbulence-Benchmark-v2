def lists_with_product_equal_n(circle_list, n=-36):
    num_elements = len(circle_list)
    for i in range(num_elements):
        product = 1
        for j in range(i, num_elements + i):
            product *= circle_list[j % num_elements]
            if product == n:
                yield circle_list[i:j % num_elements + 1]
            elif product > n:
                break
    return list(lists_with_product_equal_n(circle_list, n))