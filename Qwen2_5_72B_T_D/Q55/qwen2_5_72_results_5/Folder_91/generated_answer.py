def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == 2:
                result.append(nums[start:index + 1])
            if product > 2:
                break
    return result