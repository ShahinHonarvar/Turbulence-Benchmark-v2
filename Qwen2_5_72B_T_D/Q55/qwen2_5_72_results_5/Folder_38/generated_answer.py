def lists_with_product_equal_n(nums):
    target = -23
    n = len(nums)
    results = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= nums[index]
            if product == target:
                results.append(nums[i:index + 1])
            elif abs(product) > abs(target):
                break
    return results