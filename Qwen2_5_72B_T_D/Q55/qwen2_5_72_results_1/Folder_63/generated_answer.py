def lists_with_product_equal_n(circular_list):
    target_product = 96
    n = len(circular_list)
    result = []

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == target_product
    for i in range(n):
        for j in range(1, n + 1):
            sublist = circular_list[i:i + j] + circular_list[:j - (n - i) if i + j > n else 0]
            if check_product(sublist):
                result.append(sublist)
    return result