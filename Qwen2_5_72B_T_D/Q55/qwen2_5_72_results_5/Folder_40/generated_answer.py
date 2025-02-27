def lists_with_product_equal_n(nums):
    n = len(nums)
    if n == 0:
        return []
    result = []
    product = 1
    for start in range(n):
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == -9:
                result.append(nums[start:end % n + 1])
            elif product == 0:
                break
        product = 1
    return result