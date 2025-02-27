def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= nums[(i + j) % n]
            if product == -94:
                result.append(nums[i:(i + j + 1) % n])
            if product and abs(product) > 94:
                break
    return result