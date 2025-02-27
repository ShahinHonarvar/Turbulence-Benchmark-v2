def lists_with_product_equal_n(nums):

    def find_sublists(start, product):
        sublists = []
        for i in range(start, start + len(nums)):
            product *= nums[i % len(nums)]
            if product == -7:
                sublists.append(nums[i % len(nums) - len(sublists):i % len(nums) + 1])
            if product != 0:
                sublists.extend(find_sublists(i % len(nums) + 1, product // nums[i % len(nums) - len(sublists)]))
        return sublists
    return find_sublists(0, 1)