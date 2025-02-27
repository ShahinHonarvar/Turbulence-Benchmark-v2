def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= nums[(i + j) % n]
            if product == 49:
                result.append(nums[i:i + j + 1] if i + j + 1 <= n else nums[i:] + nums[:(i + j + 1) % n])
            elif product > 49:
                break
    return result