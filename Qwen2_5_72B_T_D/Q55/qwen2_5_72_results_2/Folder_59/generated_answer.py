def lists_with_product_equal_n(nums):
    size = len(nums)
    nums += nums
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= nums[end]
            if product == -3:
                result.append(nums[start:end + 1])
            elif abs(product) > 3:
                break
    return result