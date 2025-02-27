def lists_with_product_equal_n(nums):
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size - 1) % n
            for i in range(start, end + 1):
                product *= nums[i % n]
            if product == 18:
                results.append(nums[start:end + 1])
            product = 1
    return results