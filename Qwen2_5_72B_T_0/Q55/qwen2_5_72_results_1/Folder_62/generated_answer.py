def lists_with_product_equal_n(circular_list):
    target_product = 100
    n = len(circular_list)
    result = []

    def find_sublists(start, length):
        if length > n:
            return
        for i in range(n):
            product = 1
            for j in range(length):
                product *= circular_list[(start + j) % n]
            if product == target_product:
                result.append(circular_list[start:(start + length) % n] + circular_list[:(start + length) % n if (start + length) % n < start else 0])
            start = (start + 1) % n
    for length in range(1, n + 1):
        find_sublists(0, length)
    return result