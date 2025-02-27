def lists_with_product_equal_n(circular_list):
    target_product = 54
    n = len(circular_list)
    result = []

    def check_product(start, end, prod):
        if prod == target_product:
            result.append(circular_list[start:end if end < n else end - n])
            return True
        for i in range(start, end if end < n else end - n + 1):
            check_product(i + 1, i + 3, prod * circular_list[i])
    for i in range(n):
        check_product(i, i, circular_list[i])
    return result