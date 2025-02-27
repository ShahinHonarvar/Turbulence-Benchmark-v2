def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == 40:
                result.append(nums[start:end % n + 1] if end % n >= start else nums[start:] + nums[:end % n + 1])
            elif product == 0:
                break
    return result