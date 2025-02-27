def lists_with_product_equal_n(nums):

    def find_sublists(start, n, target, current, results):
        if target == 1 and n > 0:
            results.append(current.copy())
            return
        if start >= len(nums) or n == 0 or target < 1:
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if target % num == 0:
                current.append(num)
                find_sublists(i + 1, n - 1, target // num, current, results)
                current.pop()
    results = []
    for n in range(1, len(nums) + 1):
        find_sublists(0, n, 42, [], results)
    return results