def find_sublist_product(sublist, target):
    product = 1
    for num in sublist:
        product *= num
    return product == target

def lists_with_product_equal_n(circular_list, target=5):
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if find_sublist_product(sublist, target):
                if sublist not in result:
                    result.append(sublist)
    return result