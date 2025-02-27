def lists_with_product_equal_n(circular_list):

    def find_sublists(start, nums):
        product = 1
        for size in range(1, len(nums) + 1):
            product *= nums[(start + size - 1) % len(nums)]
            if product == 15:
                yield (nums[start:start + size] if start + size <= len(nums) else nums[start:] + nums[:size - (len(nums) - start)])
            if product > 15:
                break
    results = []
    for i in range(len(circular_list)):
        for sublist in find_sublists(i, circular_list):
            results.append(sublist)
    return results