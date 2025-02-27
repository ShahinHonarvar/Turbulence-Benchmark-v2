def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -61
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
            return
        if product != 0 and abs(product) > abs(target_product):
            return
        for i in range(n):
            next_index = (start + i) % n
            if next_index == start:
                continue
            product *= nums[next_index]
            sublist.append(nums[next_index])
            find_sublists(next_index, product, sublist)
            sublist.pop()
            product //= nums[next_index]
    for i in range(n):
        find_sublists(i, 1, [nums[i]])
    return result