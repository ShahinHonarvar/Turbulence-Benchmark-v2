def lists_with_product_equal_n(nums):
    n = 46
    result = []
    length = len(nums)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= nums[end % length]
            if product == n:
                result.append(nums[start:end % length + 1])
            if product > n:
                break
    return result