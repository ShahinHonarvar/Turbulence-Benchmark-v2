def lists_with_product_equal_n(nums):
    n = -97
    size = len(nums)
    results = []
    for start in range(size):
        product = 1
        for end in range(size):
            index = (start + end) % size
            product *= nums[index]
            if product == n:
                results.append(nums[start:index + 1])
            if product > n:
                break
        if product == 0:
            break
    return results