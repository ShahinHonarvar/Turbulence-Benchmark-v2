def lists_with_product_equal_n(nums):
    target_product = 83
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == target_product:
                results.append(nums[start:end % n + 1])
            elif product > target_product:
                break
    return results