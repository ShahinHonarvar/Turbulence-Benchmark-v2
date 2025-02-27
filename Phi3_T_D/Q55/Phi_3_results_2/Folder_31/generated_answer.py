def lists_with_product_equal_n(circular_list):
    target_product = -16
    n = len(circular_list)
    products = set()
    sublists = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[j % n]
            product = sublist if sublist == 0 else 1
            if j > i:
                product *= products.pop()
            if product == target_product:
                sublists.append(circular_list[i:j % n + 1])
                products = set([sublist])
            elif product < target_product:
                break
            products.add(sublist)
    return sublists