def all_ints_div_by_both_two_nums(int_list):
    start = 56
    end = 88
    div_by_both = [num for num in int_list[start:end + 1] if num % -59 == 0 and num % -79 == 0]
    return div_by_both