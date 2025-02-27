def lists_with_product_equal_n(nums, n=17):
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, i + len(nums)):
            product *= nums[j % len(nums)]
            sublist.append(nums[j % len(nums)])
            if product == -n:
                result.append(sublist)
            elif product > -n:
                break
    return result