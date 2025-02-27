def lists_with_product_equal_n(nums):

    def find_sublists(start, product, length):
        sublists = []
        current_product = 1
        for i in range(length):
            index = (start + i) % length
            current_product *= nums[index]
            if current_product == product:
                sublists.append(nums[start:index + 1])
        return sublists
    n = len(nums)
    all_sublists = []
    for i in range(n):
        all_sublists.extend(find_sublists(i, -75, n))
    return all_sublists