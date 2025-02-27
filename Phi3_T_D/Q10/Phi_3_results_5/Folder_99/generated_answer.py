def all_odd_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst[295:574]) if num % 2 != 0]