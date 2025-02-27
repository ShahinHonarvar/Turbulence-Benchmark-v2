def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= nums[index]
            sublist.append(nums[index])
            if product == 15:
                result.append(sublist[:])
            elif product > 15:
                break
    return result