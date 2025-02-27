def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst):
        n = len(lst)
        return [lst[i:i + j] for i in range(n) for j in range(1, n + 1)]
    sublists = circular_sublists(circular_list)
    return [sublist for sublist in sublists if sublist and product(sublist) == 48]

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result