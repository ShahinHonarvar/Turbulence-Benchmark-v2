def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(n):
            index = (start + size) % n
            product *= nums[index]
            if product == 49:
                result.append(nums[start:index + 1])
            elif product > 49:
                break
    return result