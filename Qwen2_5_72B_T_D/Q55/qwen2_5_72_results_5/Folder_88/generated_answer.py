def lists_with_product_equal_n(circular_list):

    def get_sublists(start, end, lst):
        if start < 0:
            start = len(lst) + start
        if end < 0:
            end = len(lst) + end
        if start > end:
            return lst[start:] + lst[:end]
        return lst[start:end]
    n = len(circular_list)
    result = []
    target_product = -56
    for i in range(n):
        product = 1
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            if product == target_product:
                result.append(get_sublists(i, idx + 1, circular_list))
            if abs(product) > abs(target_product):
                break
    return result