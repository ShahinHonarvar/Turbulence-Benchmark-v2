def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product == 25:
                result.append(nums[i:j + 1])
            elif product > 25:
                break
    return result