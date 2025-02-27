def lists_with_product_equal_n(nums):

    def find_sublists(start, prod, n):
        sublists = []
        current = start
        for i in range(n):
            prod *= nums[current]
            if prod == -906:
                sublists.append(nums[start:current + 1])
            current = (current + 1) % n
        return sublists
    n = len(nums)
    all_sublists = []
    for i in range(n):
        all_sublists.extend(find_sublists(i, 1, n))
    return all_sublists