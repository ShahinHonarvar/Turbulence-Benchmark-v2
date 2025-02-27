def rotate(lst, n):
    return lst[n:] + lst[:n]

def check_product(sublist):
    product = 1
    for item in sublist:
        product *= item
    return product == -3

def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    if length == 0:
        return []
    heads = circular_list
    tail_product_index = []
    current_list = heads
    current_product = -3
    while -current_product not in heads and -current_product not in current_list:
        current_list = rotate(current_list, 1)
    for i, head in enumerate(heads):
        if head == -current_product:
            tail_product_index.append(i)
    results = []
    for index in tail_product_index:
        sublist = []
        temp_list = rotate(circular_list, index)
        sublist.append(temp_list[0])
        for num in temp_list[1:]:
            if check_product(sublist + [num]):
                sublist.append(num)
            else:
                break
        results.append(sublist)
    return results