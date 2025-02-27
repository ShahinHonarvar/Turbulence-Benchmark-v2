def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == 42:
                result.append(nums[start:(end + 1) % n] + nums[:(end + 1) % n - start] if (end + 1) % n < start else nums[start:end + 1])
    return result