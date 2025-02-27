def lists_with_product_equal_n(nums):
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for end in range(start, start + n - 1):
            product *= nums[end % n]
            if product == 10:
                results.append(nums[start:end % n + 1])
            elif product == 0:
                break
    return results