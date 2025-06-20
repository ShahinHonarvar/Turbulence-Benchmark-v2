def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == -69:
                result.append(nums[start:end % n + 1] if start <= end % n else nums[start:] + nums[:end % n + 1])
    return result