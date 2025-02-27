def lists_with_product_equal_n(nums):
    target = 5
    result = []
    n = len(nums)
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == target:
                result.append(nums[start:index + 1])
            if product > target:
                break
    return result