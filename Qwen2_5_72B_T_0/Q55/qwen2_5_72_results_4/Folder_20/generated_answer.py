def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current_list):
        if product == -69:
            result.append(current_list[:])
            return
        if product != 0 and abs(product) > 69:
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if product * num == -69:
                result.append(current_list + [num])
            elif product * num != 0 and abs(product * num) < 69:
                find_sublists(i + 1, product * num, current_list + [num])
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [])
    return result