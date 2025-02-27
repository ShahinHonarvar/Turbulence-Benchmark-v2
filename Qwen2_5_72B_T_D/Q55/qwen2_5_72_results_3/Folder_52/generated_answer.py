def lists_with_product_equal_n(nums):
    target = 37
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            product *= nums[(start + i) % n]
            if product == target:
                result.append(nums[start:(start + i + 1) % n])
            elif product > target:
                break
    return result