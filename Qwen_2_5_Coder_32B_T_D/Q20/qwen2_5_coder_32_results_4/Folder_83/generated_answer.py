def find_n_th_smallest_num(numbers):
    sub_list = numbers[30:301]
    sub_list.sort()
    return sub_list[14]