def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            index = (start + i) % n
            product *= nums[index]
            if product == -9:
                result.append(nums[start:index + 1])
            if product == 0 or abs(product) > 9:
                break
    return result