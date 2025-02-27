def lists_with_product_equal_n(nums):
    target_product = 27
    n = len(nums)
    results = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= nums[(i + j) % n]
            if product == target_product:
                results.append(nums[i:(i + j + 1) % n] if (i + j + 1) % n > i else nums[i:] + nums[:(i + j + 1) % n])
            if product > target_product:
                break
    return results