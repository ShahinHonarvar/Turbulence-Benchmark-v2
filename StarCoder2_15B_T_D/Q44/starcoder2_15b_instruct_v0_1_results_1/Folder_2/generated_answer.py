def all_composite_nums(lst):
    return [num for num in lst if num > 1 and any((num % i == 0 for i in range(2, num)))]

def in_range(lst, start, end):
    return [num for i, num in enumerate(lst) if start <= i <= end]

def composite_nums_between_indices(lst):
    return set(in_range(all_composite_nums(lst), 35, 49))