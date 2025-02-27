def sum_odd_ints_inclusive(integers):
    odd_ints = [num for num in integers[31:35] if num % 2 != 0]
    return sum(odd_ints) if odd_ints else 0