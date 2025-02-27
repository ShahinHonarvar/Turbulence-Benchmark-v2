def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 91
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            product *= nums[(start + i) % n]
            if product == target_product:
                result.append(nums[start:(start + i + 1) % n] if (start + i + 1) % n > start else nums[start:] + nums[:(start + i + 1) % n])
            if product > target_product:
                break
    return result