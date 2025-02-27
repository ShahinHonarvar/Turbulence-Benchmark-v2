def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current):
        if product == 6:
            result.append(current[:])
            return
        if product > 6:
            return
        for i in range(start, start + len(nums)):
            current.append(nums[i % len(nums)])
            find_sublists(i + 1, product * nums[i % len(nums)], current)
            current.pop()
    result = []
    unique_results = set()
    for i in range(len(nums)):
        find_sublists(i, 1, [])
    for r in result:
        if tuple(r) not in unique_results:
            unique_results.add(tuple(r))
    return [list(u) for u in unique_results]