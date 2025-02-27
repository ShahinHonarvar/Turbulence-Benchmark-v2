def circular_list_next(lst, index):
    return lst[index % len(lst)]

def lists_with_product_equal_n(circular_list, target_product=22):
    result = []
    n = len(circular_list)
    for head_index in range(n):
        temp_list = []
        current_product = 1
        for tail_index in range(head_index, n * 2):
            temp_list.append(circular_list[tail_index % n])
            current_product *= circular_list[tail_index % n]
            if current_product == target_product:
                result.append(temp_list[:])
                temp_list = []
                current_product = 1
            elif current_product > target_product:
                temp_list = []
                current_product = 1
    return result