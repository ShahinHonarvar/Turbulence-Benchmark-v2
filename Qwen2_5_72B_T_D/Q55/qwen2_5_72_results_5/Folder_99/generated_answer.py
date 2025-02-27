def lists_with_product_equal_n(nums):
    n = 415
    length = len(nums)
    results = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= nums[end % length]
            if product == n:
                results.append(nums[start:end % length + 1])
            elif product > n:
                break
    return results