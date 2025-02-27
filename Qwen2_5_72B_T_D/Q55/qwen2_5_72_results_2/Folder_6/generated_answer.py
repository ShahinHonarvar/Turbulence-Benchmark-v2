def lists_with_product_equal_n(nums):
    target = 42
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == target:
                result.append(nums[start:end % n + 1])
            elif product > target:
                break
    return result