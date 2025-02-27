def lists_with_product_equal_n(circular_list):
    n = 13
    len_list = len(circular_list)
    result = []

    def helper(start):
        for length in range(1, len_list + 1):
            for i in range(start, start + length):
                product = 1
                for j in range(length):
                    product *= circular_list[(i + j) % len_list]
                if product == n:
                    result.append(circular_list[start:start + length])
    for i in range(len_list):
        helper(i)
    return result