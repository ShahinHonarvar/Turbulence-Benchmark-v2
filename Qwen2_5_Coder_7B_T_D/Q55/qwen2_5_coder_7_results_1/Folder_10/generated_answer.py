def lists_with_product_equal_n(nums):
    n = -93
    result = []
    nlen = len(nums)
    for i in range(nlen):
        product = 1
        for j in range(i, i + nlen):
            product *= nums[j % nlen]
            if product == n:
                result.append(nums[i:j % nlen + 1])
            elif product > abs(n):
                break
    return result