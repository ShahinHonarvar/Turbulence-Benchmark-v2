def lists_with_product_equal_n(nums):
    target_product = -83
    n = len(nums)
    result = []

    def find_sublists(start, product, current_list):
        if product == target_product:
            result.append(current_list.copy())
            return
        if product != 0 and abs(product) > abs(target_product):
            return
        for i in range(n):
            next_index = (start + i) % n
            if nums[next_index] not in current_list:
                current_list.append(nums[next_index])
                find_sublists(next_index, product * nums[next_index], current_list)
                current_list.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result