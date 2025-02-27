def lists_with_product_equal_n(nums):
    target_product = -82
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            for i in range(start, start + length):
                product *= nums[i % n]
            if product == target_product:
                result.append(nums[start:(start + length) % n] if start + length < n else nums[start:] + nums[:start + length - n])
            product //= nums[(start + length - 1) % n]
    return result