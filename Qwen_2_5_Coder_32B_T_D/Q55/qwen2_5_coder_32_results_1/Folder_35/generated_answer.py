def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == 83:
                result.append(nums[start % n:end % n + 1])
    return result