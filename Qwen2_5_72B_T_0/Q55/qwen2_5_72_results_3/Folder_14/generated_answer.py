def lists_with_product_equal_n(nums):

    def find_sublists(start, product, length):
        sublists = []
        current_product = 1
        for i in range(length):
            index = (start + i) % len(nums)
            current_product *= nums[index]
            if current_product == product:
                sublists.append(nums[start:index + 1])
            if current_product == 0:
                break
        return sublists
    n = len(nums)
    result = []
    for i in range(n):
        result.extend(find_sublists(i, -72, n))
    return result