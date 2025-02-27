def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            end_index = end % n
            product *= nums[end_index]
            if product == -7:
                result.append(nums[start:end_index + 1])
    return result