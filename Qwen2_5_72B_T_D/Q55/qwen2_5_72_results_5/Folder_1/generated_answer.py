def lists_with_product_equal_n(nums):
    target = -51
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == target:
                result.append(nums[start:index + 1])
            if abs(product) > target:
                break
    return result