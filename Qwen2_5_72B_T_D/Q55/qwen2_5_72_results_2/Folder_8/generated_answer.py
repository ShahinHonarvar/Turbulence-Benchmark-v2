def lists_with_product_equal_n(nums):
    n = -41
    result = []
    length = len(nums)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= nums[(i + j) % length]
            if product == n:
                result.append(nums[i:(i + j + 1) % length] if (i + j + 1) % length > i else nums[i:] + nums[:(i + j + 1) % length])
            if abs(product) > n:
                break
    return result