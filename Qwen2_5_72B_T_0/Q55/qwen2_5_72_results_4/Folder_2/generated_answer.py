def lists_with_product_equal_n(nums):
    target_product = -968
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
            if nums[index] * product == target_product:
                sublist.append(nums[index])
                result.append(sublist.copy())
                return
            if nums[index] * product != 0:
                find_sublists(index + 1, product * nums[index], sublist + [nums[index]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result