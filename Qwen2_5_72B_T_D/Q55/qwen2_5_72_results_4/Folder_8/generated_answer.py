def lists_with_product_equal_n(nums):
    target_product = -41
    n = len(nums)
    result = []

    def find_sublists(start, prod, current_list):
        if prod == target_product:
            result.append(current_list[:])
            return
        if prod != 0 and abs(prod) > abs(target_product):
            return
        for i in range(n):
            next_index = (start + i) % n
            next_num = nums[next_index]
            new_prod = prod * next_num
            current_list.append(next_num)
            find_sublists(next_index, new_prod, current_list)
            current_list.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result