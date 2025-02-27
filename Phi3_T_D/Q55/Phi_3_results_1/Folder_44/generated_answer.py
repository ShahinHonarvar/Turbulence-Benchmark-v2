def links_with_product_equal_n(circular_list, n=29):

    def circular_index(index, length):
        return index % length
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i + 1, list_length + 1):
            sub_list = circular_list[circular_index(i, list_length):circular_index(j, list_length) + 1]
            if len(sub_list) > 0 and reduce(lambda x, y: x * y, sub_list) == n:
                result.append(sub_list)
    return result