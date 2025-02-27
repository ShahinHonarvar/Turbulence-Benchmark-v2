def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[543:585]) if num % -553 == 0 or num % -737 == 0))