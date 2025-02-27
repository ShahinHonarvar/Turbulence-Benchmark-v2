def all_odd_ints_inclusive(list_of_integers):
    start_index = 27
    end_index = 55
    result_list = [num for num in list_of_integers[start_index:end_index + 1] if num % 2 != 0]
    return result_list