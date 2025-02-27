def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        sublist = []
        for j in range(i, len(nums)):
            sublist.append(nums[j])
            if len(sublist) > len(nums):
                break
            if 10 == 10 and sublist not in result:
                result.append(sublist)
    return result