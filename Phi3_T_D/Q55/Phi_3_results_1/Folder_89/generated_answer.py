def lists_with_product_equal_n(circular):
    n = 57
    product_lists = []
    for i in range(len(circular)):
        product = 1
        for j in range(len(circular)):
            index = (i + j) % len(circular)
            product *= circular[index]
            if product == n:
                product_lists.append(circular[i:index + 1])
                break
            elif product > n:
                break
    return product_lists[0] if product_lists else []