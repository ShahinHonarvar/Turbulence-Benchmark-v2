def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []

    def check_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -26
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length]
            if len(sublist) < length:
                sublist += circular_list[:length - len(sublist)]
            if check_sublist(sublist):
                results.append(sublist)
    return results