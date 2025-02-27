def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == -33:
                result.append(nums[start:end % n + 1] if end % n >= start else nums[start:] + nums[:end % n + 1])
    return result