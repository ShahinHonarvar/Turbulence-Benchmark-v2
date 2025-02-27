def lists_with_product_equal_n(nums):
    target_product = 57
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            idx = (start + end) % n
            product *= nums[idx]
            if product == target_product:
                result.append(nums[start:idx + 1] if start <= idx else nums[start:] + nums[:idx + 1])
            elif product > target_product:
                break
    return result