def lists_with_product_equal_n(nums):
    target_product = 76
    sublists = []
    n = len(nums)
    for start in range(n):
        product = 1
        list_len = 0
        temp_list = []
        for end in range(start, start + n):
            index = end % n
            temp_list.append(nums[index])
            product *= nums[index]
            list_len += 1
            if product == target_product:
                sublists.append(temp_list)
            elif product > target_product:
                break
    return sublists