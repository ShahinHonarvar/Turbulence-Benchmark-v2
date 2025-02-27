def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            idx = (start + end) % n
            product *= nums[idx]
            if product == -30:
                result.append(nums[start:idx + 1] if start <= idx else nums[start:] + nums[:idx + 1])
            if product == 0:
                break
    return result