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
        for i in range(1, n + 1):
            next_index = (start + i - 1) % n
            if nums[next_index] * product == target_product:
                result.append(sublist + [nums[next_index]])
            elif nums[next_index] * product != 0:
                find_sublists(next_index, nums[next_index] * product, sublist + [nums[next_index]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result