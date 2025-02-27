def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -75
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            for i in range(start, start + length):
                product *= nums[i % n]
            if product == target_product:
                result.append(nums[start:start + length])
            product = 1
    return result