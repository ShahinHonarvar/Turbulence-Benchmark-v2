def lists_with_product_equal_n(nums):

    def find_sublists(start, prod, current):
        if prod == -54:
            result.append(current[:])
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if prod * num == -54:
                result.append(current + [num])
            elif prod * num > -54 and num != 0:
                find_sublists(i + 1, prod * num, current + [num])
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [])
    return result