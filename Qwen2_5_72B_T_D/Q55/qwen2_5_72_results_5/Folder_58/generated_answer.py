def lists_with_product_equal_n(nums):
    n = 733
    size = len(nums)
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= nums[end % size]
            if product == n:
                result.append(nums[start:end % size + 1])
            elif product > n:
                break
    return result