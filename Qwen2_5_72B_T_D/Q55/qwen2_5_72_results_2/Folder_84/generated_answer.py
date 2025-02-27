def lists_with_product_equal_n(nums):
    target_product = -906
    n = len(nums)
    result = []

    def circular_sublist_product(start, length):
        product = 1
        for i in range(length):
            product *= nums[(start + i) % n]
        return product
    for i in range(n):
        for length in range(1, n + 1):
            if circular_sublist_product(i, length) == target_product:
                sublist = nums[i:i + length] if i + length <= n else nums[i:n] + nums[0:(i + length) % n]
                result.append(sublist)
    return result