def lists_with_product_equal_n(nums):
    target = 27
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == target:
                results.append(nums[start:index + 1])
            elif product > target:
                break
    return results