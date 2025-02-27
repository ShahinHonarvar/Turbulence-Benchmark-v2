def lists_with_product_equal_n(circular_list):

    def find_sublists(start, target, current_product, length):
        sublists = []
        for i in range(1, length + 1):
            current_product *= circular_list[(start + i - 1) % length]
            if current_product == target:
                sublists.append(circular_list[start:(start + i) % length])
            elif current_product > target:
                break
        return sublists
    result = []
    n = len(circular_list)
    for start in range(n):
        result.extend(find_sublists(start, 100, 1, n))
    return result