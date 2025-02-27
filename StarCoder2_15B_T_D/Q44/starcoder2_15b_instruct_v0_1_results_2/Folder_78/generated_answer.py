def composite_nums_between_indices(lst):
    return {num for num in lst if all((num % i != 0 for i in range(2, num))) and 70 <= lst.index(num) <= 84}