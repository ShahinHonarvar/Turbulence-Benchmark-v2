def lists_with_product_equal_n(circular_list):
    target_product = -115
    n = len(circular_list)
    results = []

    def find_sublists(start, length):
        if length > n:
            return
        for i in range(n):
            product = 1
            for j in range(length):
                product *= circular_list[(start + j) % n]
            if product == target_product:
                results.append(circular_list[start:(start + length) % n] + circular_list[:(start + length) % n])
            start = (start + 1) % n
    for length in range(1, n + 1):
        find_sublists(0, length)
    return results