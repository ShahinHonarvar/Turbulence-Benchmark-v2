def lists_with_product_equal_n(circular_list):
    target_product = 100
    length = len(circular_list)
    possible_sublists = []
    for start in range(length):
        for end in range(start, length):
            sublist = circular_list[start:] + circular_list[:start]
            for i in range(length):
                possible_product = 1
                for j in range(i, i + end - start + 1):
                    possible_product *= sublist[j % length]
                    if possible_product == target_product:
                        possible_sublists.append(sublist[i:i + j - i + 1])
                        break
                    elif possible_product > target_product:
                        break
    return possible_sublists