def lists_with_product_equal_n(nums):

    def find_sublists(start, product):
        result = []
        n = len(nums)
        for i in range(start, start + n):
            product *= nums[i % n]
            if product == -10:
                result.append(nums[i % n - (n - 1):i % n + 1])
            if product == 0 or abs(product) > 10:
                break
        return result
    all_sublists = []
    for i in range(len(nums)):
        all_sublists.extend(find_sublists(i, 1))
    return all_sublists