def lists_with_product_equal_n(circular_list):

    def sublists_with_product(lst):
        n = len(lst)
        result = []
        for start in range(n):
            product = 1
            for end in range(start, n):
                product *= lst[end]
                if product == -69:
                    result.append(lst[start:end + 1])
        return result
    n = len(circular_list)
    result = []
    for i in range(n):
        rotated_list = circular_list[i:] + circular_list[:i]
        result.extend(sublists_with_product(rotated_list))
    return result