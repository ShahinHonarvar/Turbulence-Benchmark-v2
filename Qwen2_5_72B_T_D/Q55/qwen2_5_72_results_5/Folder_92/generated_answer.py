def lists_with_product_equal_n(nums):
    target_product = 5
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[i:index + 1])
            elif product > target_product:
                break
    return result