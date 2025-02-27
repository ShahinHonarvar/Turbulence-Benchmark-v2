def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(n):
            index = (start + size) % n
            product *= nums[index]
            if product == 0:
                result.append(nums[start:index + 1])
            if product != 0 and 0 in nums[start:index + 1]:
                break
    return result