def lists_with_product_equal_n(nums, n):
    result = []
    for i in range(len(nums)):
        sublist = [nums[i]]
        product = nums[i]
        j = (i + 1) % len(nums)
        while product < n:
            sublist.append(nums[j])
            product *= nums[j]
            j = (j + 1) % len(nums)
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result