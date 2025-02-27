def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= nums[index]
            if product == -690:
                result.append(nums[start:index + 1])
    return result