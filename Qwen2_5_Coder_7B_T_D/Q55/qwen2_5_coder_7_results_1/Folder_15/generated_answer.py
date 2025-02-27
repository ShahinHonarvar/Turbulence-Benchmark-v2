def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= nums[j % n]
            if product == -7:
                result.append(nums[i:j % n])
    return result