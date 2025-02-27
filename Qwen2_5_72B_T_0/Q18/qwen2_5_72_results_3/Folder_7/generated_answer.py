def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[543:585]) if x % -553 == 0 or x % -737 == 0))