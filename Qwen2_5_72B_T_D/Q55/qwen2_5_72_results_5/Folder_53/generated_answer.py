def lists_with_product_equal_n(nums):

    def find_sublists(start, product):
        sublists = []
        current_product = 1
        for i in range(len(nums)):
            index = (start + i) % len(nums)
            current_product *= nums[index]
            if current_product == product:
                sublists.append(nums[start:index + 1])
            elif abs(current_product) > abs(product):
                break
        return sublists
    target_product = -87
    all_sublists = []
    for start in range(len(nums)):
        all_sublists.extend(find_sublists(start, target_product))
    return all_sublists