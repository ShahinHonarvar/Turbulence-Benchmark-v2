def lists_with_product_equal_n(nums):
    target_product = -81
    n = len(nums)
    result = []

    def check_sublist(start, length):
        product = 1
        for i in range(length):
            product *= nums[(start + i) % n]
        return product == target_product
    for start in range(n):
        for length in range(1, n + 1):
            if check_sublist(start, length):
                sublist = [nums[(start + i) % n] for i in range(length)]
                result.append(sublist)
    return result