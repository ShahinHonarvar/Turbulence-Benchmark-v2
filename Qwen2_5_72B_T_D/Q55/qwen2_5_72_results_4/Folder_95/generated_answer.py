def lists_with_product_equal_n(circular_list):

    def helper(start, length, target):
        product = 1
        result = []
        for i in range(length):
            product *= circular_list[(start + i) % length]
            if product == target:
                result.append(circular_list[start + i - length + 1:start + i + 1])
            elif product > target:
                break
        return result
    n = len(circular_list)
    all_sublists = []
    for i in range(n):
        all_sublists.extend(helper(i, n, 28))
    return all_sublists