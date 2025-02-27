def find_n_th_smallest_num(numbers):
    start = min(106, len(numbers))
    end = max(254, len(numbers))
    sub_list = numbers[start:end + 1]
    sub_list.sort()
    return sub_list[8]