def lists_with_product_equal_n(nums):

    def find_sublists(start, product, target, length):
        sublists = []
        current_list = []
        for i in range(length):
            num = nums[(start + i) % length]
            product *= num
            current_list.append(num)
            if product == target:
                sublists.append(current_list.copy())
            elif abs(product) > abs(target):
                break
        return sublists
    target = -83
    length = len(nums)
    result = []
    for i in range(length):
        result.extend(find_sublists(i, 1, target, length))
    return result