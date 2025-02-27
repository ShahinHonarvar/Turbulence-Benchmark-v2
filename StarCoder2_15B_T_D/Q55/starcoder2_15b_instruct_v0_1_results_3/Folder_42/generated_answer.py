def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(start, start + n):
            index = i % n
            product *= nums[index]
            sublist.append(nums[index])
            if product == 25:
                result.append(sublist)
                break
            elif product > 25:
                break
    return result