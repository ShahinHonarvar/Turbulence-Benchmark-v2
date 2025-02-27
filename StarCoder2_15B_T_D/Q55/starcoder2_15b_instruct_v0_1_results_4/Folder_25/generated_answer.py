def lists_with_product_equal_n(nums):
    n = -32
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, len(nums)):
            product *= nums[j]
            sublist.append(nums[j])
            if product == n:
                result.append(sublist)
            if product < n:
                continue
            else:
                break
    return result