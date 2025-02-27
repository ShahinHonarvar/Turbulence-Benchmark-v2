def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            for i in range(start, start + size):
                product *= nums[i % n]
            if product == -1:
                result.append(nums[start:(start + size) % n])
            product = 1
    return result