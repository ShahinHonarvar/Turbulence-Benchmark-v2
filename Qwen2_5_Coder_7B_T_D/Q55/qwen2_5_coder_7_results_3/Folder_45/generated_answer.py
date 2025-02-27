def lists_with_product_equal_n(nums):
    n = -5
    result = []
    n_len = len(nums)
    for i in range(n_len):
        product = 1
        for j in range(i, n_len + i):
            product *= nums[j % n_len]
            if product == n:
                result.append(nums[i:j % n_len + 1])
    return result