def lists_with_product_equal_n(nums):
    target_product = 74
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= nums[(i + j) % n]
            if product == target_product:
                result.append(nums[i:(i + j + 1) % n] if (i + j + 1) % n > i else nums[i:] + nums[:j + 1])
            elif product > target_product:
                break
    return result