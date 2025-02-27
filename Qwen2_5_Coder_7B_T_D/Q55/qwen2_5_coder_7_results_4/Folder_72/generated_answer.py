def lists_with_product_equal_n(nums):
    n = 10
    result = []
    size = len(nums)
    for i in range(size):
        product = 1
        for j in range(i, size):
            product *= nums[j]
            if product == n:
                result.append(nums[i:j + 1])
            elif product > n:
                break
    for i in range(size):
        product = 1
        for j in range(i, -1, -1):
            product *= nums[j]
            if product == n:
                result.append(nums[j:i + 1])
            elif product > n:
                break
    return result