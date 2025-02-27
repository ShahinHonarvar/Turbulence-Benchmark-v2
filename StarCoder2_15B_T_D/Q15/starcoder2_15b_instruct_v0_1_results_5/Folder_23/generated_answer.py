def sum_odd_ints_inclusive(int_list):
    odd_ints = [n for n in int_list[52:72] if n % 2 == 1]
    return sum(odd_ints) if odd_ints else 0