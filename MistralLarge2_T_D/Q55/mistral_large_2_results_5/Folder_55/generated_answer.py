def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def extend_list(lst, idx, target):
        product = 1
        sublist = []
        for i in range(n):
            product *= lst[(idx + i) % n]
            sublist.append(lst[(idx + i) % n])
            if product == target:
                result.append(sublist[:])
            if product == 0:
                break
    for i in range(n):
        extend_list(circular_list, i, -6)
    return result