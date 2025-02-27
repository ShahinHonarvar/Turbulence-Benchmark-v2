def lists_with_product_equal_n(nums):
    target_product = 632
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            product *= nums[(start + i) % n]
            if product == target_product:
                result.append(nums[start:(start + i + 1) % n])
            elif product > target_product:
                break
    return result