def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        window = []
        product = 1
        for j in range(i, i + n):
            index = j % n
            window.append(nums[index])
            product *= nums[index]
            if product == -72:
                result.append(window.copy())
            if product == 0:
                break
    return result