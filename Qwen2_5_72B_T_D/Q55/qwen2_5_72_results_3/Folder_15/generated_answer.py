def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for start in range(n):
        product = 1
        for end in range(n):
            product *= nums[(start + end) % n]
            if product == -7:
                result.append(nums[start:(start + end + 1) % n] if (start + end + 1) % n > start else nums[start:] + nums[:(start + end + 1) % n])
            elif abs(product) > 7:
                break
    return result