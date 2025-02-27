def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 93
    result = []

    def has_product_equal_to_target(start, end):
        product = 1
        for i in range(start, end):
            index = i % n
            product *= nums[index]
            if product == target_product:
                result.append(nums[start:start + (i - start) + 1])
    for i in range(n):
        for j in range(1, n + 1):
            has_product_equal_to_target(i, i + j)
    return result