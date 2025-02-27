def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 10:
        return []
    relevant_ints = int_list[6:10]
    divisible_ints = [num for num in relevant_ints if num % -1 == 0 and num % -10 == 0]
    return divisible_ints