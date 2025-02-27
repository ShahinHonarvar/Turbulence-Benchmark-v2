def lists_with_product_equal_n(nums):
    target_product = 32
    length = len(nums)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= nums[end % length]
            if product == target_product:
                result.append(nums[start:end % length + 1])
            elif product > target_product:
                break
    return result