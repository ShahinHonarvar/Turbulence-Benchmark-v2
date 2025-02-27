from itertools import permutations

def lists_with_product_equal_n(circular_list):

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 8

    def make_circular(lst):
        return lst + lst[:-1]
    circular_list = make_circular(circular_list)
    result = []
    for i in range(len(circular_list)):
        for size in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + size]
            if check_product(sublist) and sublist not in result:
                result.append(sublist)
    return result