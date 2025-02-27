def lists_with_product_equal_n(lst):
    n, product_lists = (28, [])
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j] + lst[:i]
            if i and j == len(lst):
                sublist = sublist[1:] + sublist[:1]
            if n == prod(sublist):
                product_lists.append(sublist)
    return product_lists

def prod(nums):
    result = 1
    for num in nums:
        result *= num
    return result