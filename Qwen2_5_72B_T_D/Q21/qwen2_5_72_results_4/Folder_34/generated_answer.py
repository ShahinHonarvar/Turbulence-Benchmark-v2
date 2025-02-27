def all_ints_div_by_num(lst):
    start_index = 30
    end_index = 30
    result = [num for num in lst[start_index:end_index + 1] if num % 3 == 0]
    return result