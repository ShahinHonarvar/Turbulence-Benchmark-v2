def lists_with_product_equal_n(nums):

    def find_sublists(start, product, target, length):
        sublists = []
        current = start
        for i in range(length):
            product *= nums[current]
            if product == target:
                sublists.append(nums[start:current + 1])
            current = (current + 1) % length
            if product > target:
                break
        return sublists
    n = len(nums)
    all_sublists = []
    for i in range(n):
        all_sublists.extend(find_sublists(i, 1, 18, n))
    return all_sublists