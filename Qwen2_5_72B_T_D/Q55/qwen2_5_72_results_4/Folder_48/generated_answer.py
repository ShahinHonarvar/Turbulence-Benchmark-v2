def lists_with_product_equal_n(circular_list):
    target_product = 990
    n = len(circular_list)
    result = []

    def check_product(start, end):
        product = 1
        for i in range(start, end + 1):
            product *= circular_list[i % n]
        return product == target_product
    for start in range(n):
        for end in range(start, start + n):
            if check_product(start, end):
                sublist = circular_list[start:end + 1]
                if len(sublist) <= n:
                    result.append(sublist)
    return result