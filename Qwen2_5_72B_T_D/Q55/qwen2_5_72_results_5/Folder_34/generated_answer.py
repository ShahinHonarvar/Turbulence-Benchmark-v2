def lists_with_product_equal_n(nums):
    n = -81
    result = []
    length = len(nums)
    for start in range(length):
        product = 1
        for end in range(length):
            product *= nums[(start + end) % length]
            if product == n:
                result.append(nums[start:(start + end + 1) % length] if (start + end + 1) % length > start else nums[start:length] + nums[0:(start + end + 1) % length])
            elif abs(product) > abs(n):
                break
    return result