def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -93
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[i:index + 1])
            if product == 0 or abs(product) > abs(target_product):
                break
    return result