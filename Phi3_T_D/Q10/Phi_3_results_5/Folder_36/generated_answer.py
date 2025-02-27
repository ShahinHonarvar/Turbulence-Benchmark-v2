def all_odd_ints_exclusive(lst):
    return [num for index, num in enumerate(lst[598:767], start=598) if num % 2 != 0]