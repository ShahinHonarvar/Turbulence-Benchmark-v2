def lists_with_product_equal_n(nums):

    def sublists_with_product(arr, target):
        result = []
        for start in range(len(arr)):
            product = 1
            for end in range(start, len(arr)):
                product *= arr[end]
                if product == target:
                    result.append(arr[start:end + 1])
                elif product < target:
                    continue
                else:
                    break
        return result
    circular_nums = nums + nums
    all_sublists = []
    for i in range(len(nums)):
        sublists = sublists_with_product(circular_nums[i:i + len(nums)], -6)
        for sublist in sublists:
            if sublist not in all_sublists:
                all_sublists.append(sublist)
    return all_sublists