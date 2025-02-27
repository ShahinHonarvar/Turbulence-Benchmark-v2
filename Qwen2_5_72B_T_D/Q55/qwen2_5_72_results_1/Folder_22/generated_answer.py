def lists_with_product_equal_n(nums):

    def find_sublists(start, product):
        sublists = []
        n = len(nums)
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == 4:
                sublists.append(nums[start:index + 1])
            elif product > 4:
                break
        return sublists
    all_sublists = []
    for i in range(len(nums)):
        all_sublists.extend(find_sublists(i, 1))
    return all_sublists