def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    target_product = -69
    for start in range(n):
        product = 1
        for i in range(n):
            index = (start + i) % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[start:index + 1])
            if product == 0 or abs(product) > abs(target_product):
                break
    return result