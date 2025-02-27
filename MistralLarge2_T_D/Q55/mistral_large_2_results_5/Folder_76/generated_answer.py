def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst):
        n = len(lst)
        sublists = []
        for i in range(n):
            for j in range(i + 1, i + n + 1):
                sublists.append(lst[i:j % n if j % n != 0 else n])
        return sublists
    sublists = circular_sublists(circular_list)
    result = [sublist for sublist in sublists if sublist and product(sublist) == 247]
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod