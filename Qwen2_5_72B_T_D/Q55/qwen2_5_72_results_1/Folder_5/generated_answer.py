def lists_with_product_equal_n(nums):

    def find_sublists(start, product, n):
        sublists = []
        current_product = 1
        for i in range(n):
            current_product *= nums[(start + i) % n]
            if current_product == product:
                sublists.append(nums[(start + i - n + 1) % n:(start + i + 1) % n])
        return sublists
    n = len(nums)
    all_sublists = []
    for start in range(n):
        all_sublists.extend(find_sublists(start, -33, n))
    return all_sublists