def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == 78:
                result.append(nums[start:(end + 1) % n] if (end + 1) % n > start else nums[start:] + nums[:(end + 1) % n])
            elif product > 78:
                break
    return result