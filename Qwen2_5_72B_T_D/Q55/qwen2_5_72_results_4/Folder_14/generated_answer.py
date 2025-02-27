def lists_with_product_equal_n(nums):

    def find_sublists(start, product):
        for i in range(start, start + len(nums)):
            product *= nums[i % len(nums)]
            if product == -72:
                sublists.append(nums[start:i + 1])
            elif abs(product) > 72:
                break
    sublists = []
    for i in range(len(nums)):
        find_sublists(i, 1)
    return sublists