def lists_with_product_equal_n(circular_list):

    def find_sublists(start, length):
        sublists = []
        current_product = 1
        for i in range(length):
            current_product *= circular_list[(start + i) % length]
            if current_product == 2:
                sublists.append(circular_list[start:start + i + 1])
        return sublists
    result = []
    n = len(circular_list)
    for i in range(n):
        result.extend(find_sublists(i, n))
    return result