def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -81
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
            return
        if product != 0 and abs(product) > abs(target_product):
            return
        for i in range(n):
            index = (start + i) % n
            if index == start and len(sublist) > 0:
                break
            find_sublists(index, product * nums[index], sublist + [nums[index]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result