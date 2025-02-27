def lists_with_product_equal_n(nums):
    n = -30
    result = []
    length = len(nums)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= nums[j % length]
            if product == n:
                result.append(nums[i:j % length + 1])
                break
    return result