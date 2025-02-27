def lists_with_product_equal_n(nums):
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == 25:
                results.append(nums[start % n:end % n + 1])
            elif product > 25:
                break
    return results