def circular_shift(lst):
    return lst[1:] + lst[:1]

def generate_sublists(lst):
    sublists = []
    for i in range(len(lst)):
        temp_product = 1
        for j in range(i, len(lst) + i):
            temp_product *= lst[j % len(lst)]
            if temp_product == 99:
                sublists.append(lst[i:j % len(lst) + 1])
            if temp_product > 99:
                break
    return sublists

def lists_with_product_equal_n(lst):
    result = []
    temp_lst = list(lst)
    for _ in range(len(lst)):
        sublists = generate_sublists(temp_lst)
        for sublist in sublists:
            if sublist not in result:
                result.append(sublist)
        temp_lst = circular_shift(temp_lst)
    return result