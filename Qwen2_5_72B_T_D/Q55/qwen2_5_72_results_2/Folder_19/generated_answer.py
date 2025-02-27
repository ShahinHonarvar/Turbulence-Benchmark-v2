def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -54
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[start:index + 1])
            if product == 0 or abs(product) > abs(target_product):
                break
    return result