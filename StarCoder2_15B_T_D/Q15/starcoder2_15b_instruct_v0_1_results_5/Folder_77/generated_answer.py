def sum_odd_ints_inclusive(int_list):
    range_ints = int_list[527:539]
    odd_ints = [num for num in range_ints if num % 2 == 1]
    sum_ints = sum(odd_ints)
    return sum_ints if odd_ints else 0