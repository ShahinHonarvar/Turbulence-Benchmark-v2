def get_circular_index(index, size):
    return index % size

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    target = -906
    result = []
    for i in range(size):
        for j in range(i, size):
            temp_product = 1
            temp_list = []
            for k in range(i, j + 1):
                temp_product *= circular_list[get_circular_index(k, size)]
                temp_list.append(circular_list[get_circular_index(k, size)])
            if temp_product == target:
                result.append(temp_list)
    return result