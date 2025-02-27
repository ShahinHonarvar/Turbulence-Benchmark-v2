def lists_with_product_equal_n(nums):
    n = -72
    result = []
    length = len(nums)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= nums[j]
            if product == n:
                result.append(nums[i:j + 1])
            elif product > n:
                break
    return result