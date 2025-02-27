def lists_with_product_equal_n(nums):
    target_product = -938
    n = len(nums)
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
            return
        if product != 0 and target_product % product != 0:
            return
        for i in range(n):
            index = (start + i) % n
            if index == start and len(sublist) > 0:
                break
            product *= nums[index]
            sublist.append(nums[index])
            find_sublists(start, product, sublist)
            product //= nums[index]
            sublist.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result