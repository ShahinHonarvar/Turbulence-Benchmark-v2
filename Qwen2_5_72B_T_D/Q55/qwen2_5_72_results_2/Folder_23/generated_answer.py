def lists_with_product_equal_n(nums):
    target_product = -95
    n = len(nums)
    result = []

    def find_sublists(start, product, current_list):
        if product == target_product:
            result.append(current_list.copy())
            return
        if product != 0 and target_product % product != 0:
            return
        for i in range(n):
            next_index = (start + i) % n
            if nums[next_index] * product == target_product:
                current_list.append(nums[next_index])
                result.append(current_list.copy())
                return
            elif next_index == start:
                break
            current_list.append(nums[next_index])
            find_sublists(next_index + 1, product * nums[next_index], current_list)
            current_list.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return result