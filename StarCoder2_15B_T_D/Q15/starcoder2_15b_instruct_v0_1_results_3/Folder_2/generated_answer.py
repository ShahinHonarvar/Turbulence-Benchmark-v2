def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for num in lst[15:40]:
        if num % 2 == 1:
            sum_odd += num
    return sum_odd