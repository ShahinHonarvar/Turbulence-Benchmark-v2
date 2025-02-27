def lists_with_product_equal_n(nums):
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, i + len(nums)):
            index = j % len(nums)
            product *= nums[index]
            sublist.append(nums[index])
            if product == 32:
                yield sublist
            elif product > 32:
                break