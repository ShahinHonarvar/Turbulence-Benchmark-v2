def lists_with_product_equal_n(nums):
    target_product = 40
    n = len(nums)
    result = []

    def check_sublist_product(start, length):
        product = 1
        for i in range(length):
            product *= nums[(start + i) % n]
        return product == target_product
    for i in range(n):
        for length in range(1, n + 1):
            if check_sublist_product(i, length):
                result.append(nums[i:i + length] if i + length <= n else nums[i:] + nums[:length - (n - i)])
    return result