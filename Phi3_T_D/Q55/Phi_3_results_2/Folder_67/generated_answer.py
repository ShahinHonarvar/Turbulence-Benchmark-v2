def lists_with_product_equal_n(circular_list):
    target = 33
    length = len(circular_list)
    product = 1
    sublists = []
    for i in range(length):
        product *= circular_list[i]
        for j in range(length):
            product //= circular_list[j]
            if product == target:
                sublist = circular_list[j:i + 1]
                while sublist[-1] < sublist[0]:
                    sublist.pop(0)
                sublists.append(sublist)
            product *= circular_list[(j + 1) % length]
    sublists = [sublist for sublist in sublists if len(sublist) <= length and any((subsub for subsub in sublists if subsub != sublist and subsub == sublist))]
    return sublists