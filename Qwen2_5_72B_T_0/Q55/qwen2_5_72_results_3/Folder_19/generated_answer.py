def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current, result):
        if product == -54:
            result.append(current[:])
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if product * num == -54:
                result.append(current + [num])
            elif product * num != 0:
                find_sublists(i + 1, product * num, current + [num], result)
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [], result)
    return result