def lists_with_product_equal_n(circular_list):
    n = -69
    result = []
    size = len(circular_list)

    def has_zero(sublist):
        return any((x == 0 for x in sublist))

    def check_all_contiguous_sublists(start):
        for length in range(1, size + 1):
            product = 1
            for i in range(length):
                product *= circular_list[(start + i) % size]
            if product == n:
                sublist = circular_list[start:start + length]
                if not has_zero(sublist) or not result or sublist != result[-1]:
                    result.append(circular_list[start:start + length])
            elif product > n:
                break
    for start in range(size):
        check_all_contiguous_sublists(start)
    return result