def lists_with_product_equal_n(nums):
    target = 53
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= nums[index]
            if product == target:
                result.append(nums[i:index + 1])
            elif product > target:
                break
    return result