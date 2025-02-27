def lists_with_product_equal_n(nums):
    target_product = 990
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for current in range(n):
            product *= nums[(start + current) % n]
            if product == target_product:
                result.append(nums[start:(start + current + 1) % n])
            elif product > target_product:
                break
    return result