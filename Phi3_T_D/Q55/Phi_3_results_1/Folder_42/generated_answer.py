def lists_with_product_equal_n(circular_list):
    result = []
    product = 25
    for i in range(len(circular_list)):
        sublist = []
        for j in range(i, len(circular_list) + i):
            sublist.append(circular_list[j % len(circular_list)])
            current_product = 1
            for num in sublist:
                current_product *= num
            if current_product == product and sublist not in result:
                result.append(sublist.copy())
        if len(sublist) > 1 and sublist[0] == sublist[-1]:
            break
    return result