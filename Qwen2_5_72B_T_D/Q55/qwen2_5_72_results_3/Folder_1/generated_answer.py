def lists_with_product_equal_n(nums):

    def check_combinations(start, length):
        sublists = []
        for size in range(1, length + 1):
            product = 1
            for i in range(size):
                product *= nums[(start + i) % length]
            if product == -51:
                sublists.append(nums[start:(start + size) % length])
            else:
                new_start = (start + size - 1) % length
                new_length = length - size + 1
                sublists.extend(check_combinations(new_start, new_length))
        return sublists
    n = len(nums)
    if n == 0:
        return []
    all_sublists = check_combinations(0, n)
    unique_sublists = list(set((tuple(sorted(sublist)) for sublist in all_sublists)))
    return [list(sublist) for sublist in unique_sublists]