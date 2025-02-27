def lists_with_product_equal_n(nums):
    target_product = -938
    n = len(nums)
    result = []

    def find_sublists(start, product, current_list):
        if product == target_product:
            result.append(current_list.copy())
            return
        if product != 0 and target_product % product != 0:
            return
        for i in range(1, n + 1):
            next_index = (start + i) % n
            next_product = product * nums[next_index]
            if next_product == 0 and target_product != 0:
                break
            current_list.append(nums[next_index])
            find_sublists(next_index, next_product, current_list)
            current_list.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result