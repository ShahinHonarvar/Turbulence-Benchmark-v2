def lists_with_product_equal_n(nums):
    target_product = -115
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            for i in range(start, start + size):
                product *= nums[i % n]
            if product == target_product:
                result.append(nums[start:(start + size) % n])
            product = 1
    return result