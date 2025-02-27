def lists_with_product_equal_n(nums):
    size = len(nums)
    target_product = 25
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= nums[end % size]
            if product == target_product:
                result.append(nums[start:end % size + 1])
            elif product > target_product:
                break
    return result