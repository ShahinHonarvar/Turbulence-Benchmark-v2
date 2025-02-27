def get_next_index(index, length):
    return index % length

def lists_with_product_equal_n(numbers):
    sublists = []
    length = len(numbers)
    zero_indexes = []
    for i in range(length):
        product = 1
        if numbers[i] == 0:
            zero_indexes.append(i)
        else:
            j = i
            sublist = []
            while product not in {1, 36} and numbers[j] != 0:
                product *= numbers[j]
                sublist.append(numbers[j])
                j = get_next_index(j, length)
            if product == 36:
                sublists.append(sublist)
    return sublists