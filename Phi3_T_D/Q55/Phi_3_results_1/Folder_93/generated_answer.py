def lists_with_product_equal_n(nums, target=91):
    if not nums:
        return []
    circular_nums = nums + nums[0:1]
    sublists = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, len(nums) + i):
            product *= circular_nums[j % len(nums)]
            sublist.append(circular_nums[j % len(nums)])
            if product == -target:
                sublists.append(sublist[:])
            if product > -target:
                break
    return sublists