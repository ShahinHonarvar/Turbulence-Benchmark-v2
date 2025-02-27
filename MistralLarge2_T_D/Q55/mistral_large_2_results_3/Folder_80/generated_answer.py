def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def find_sublists(start_index):
        product = 1
        for i in range(n):
            product *= circular_list[(start_index + i) % n]
            if product == 43:
                result.append(circular_list[start_index:start_index + i + 1])
                if start_index + i + 1 > n:
                    result[-1] += circular_list[:(start_index + i + 1) % n]
    for i in range(n):
        find_sublists(i)
    return result