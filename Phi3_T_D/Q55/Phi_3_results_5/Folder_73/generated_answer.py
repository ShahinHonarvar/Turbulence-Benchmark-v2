def lists_with_product_equal_n(circular_list, n=40):
    length = len(circular_list)
    result = []

    def product_of_list(start_idx):
        product = 1
        for i in range(length):
            idx = (start_idx + i) % length
            product *= circular_list[idx]
            if product > n:
                return None
            if product == n:
                result.append(circular_list[start_idx:start_idx + i + 1])
    for i in range(length):
        product_of_list(i)
    return result