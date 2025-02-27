def lists_with_product_equal_n(lst):

    def product(nums):
        p = 1
        for num in nums:
            p *= num
        return p
    n = len(lst)
    result = []
    found = False
    for i in range(n):
        for j in range(i, i + n):
            sublist = lst[i:j]
            if product(sublist) == 78:
                result.append(sublist)
                found = True
            if j == n - 1 and found:
                break
    if not found:
        return []
    return result