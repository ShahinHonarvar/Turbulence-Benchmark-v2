def lists_with_product_equal_n(nums):

    def find_sublists(start, current_product, current_sublist):
        if current_product == -83:
            result.append(current_sublist[:])
        if current_product != 0 and abs(current_product) < 83:
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if num * current_product != 0 and 83 % (num * current_product) == 0:
                find_sublists(i + 1, num * current_product, current_sublist + [num])
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [])
    return result