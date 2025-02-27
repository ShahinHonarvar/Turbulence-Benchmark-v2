def lists_with_product_equal_n(nums):
    target = -690
    n = len(nums)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(size):
                if i + j < n:
                    product *= nums[i + j]
            if product == target:
                result.append(nums[i:i + size])
        if n < size:
            break
    return result