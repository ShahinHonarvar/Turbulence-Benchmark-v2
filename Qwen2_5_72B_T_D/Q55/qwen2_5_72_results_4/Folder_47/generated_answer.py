def lists_with_product_equal_n(nums):
    target_product = -94
    n = len(nums)
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
            return
        if product != 0 and abs(product) > abs(target_product):
            return
        for i in range(n):
            new_start = (start + i) % n
            if new_start == start:
                continue
            find_sublists(new_start, product * nums[new_start], sublist + [nums[new_start]])
    for i in range(n):
        find_sublists(i, nums[i], [nums[i]])
    return result