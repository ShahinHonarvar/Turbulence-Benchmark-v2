def lists_with_product_equal_n(nums):
    n = 53
    result = []
    length = len(nums)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            index = j % length
            product *= nums[index]
            if product == n:
                result.append(nums[i:index + 1])
            elif product % n != 0:
                break
    return result