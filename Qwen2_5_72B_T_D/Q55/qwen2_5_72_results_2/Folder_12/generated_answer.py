def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end]
            if product == -18:
                result.append(nums[start:end + 1])
            elif abs(product) > 18:
                break
    return result