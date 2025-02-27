def all_odd_ints_inclusive(integers):
    start_index, end_index = (80, 200)
    odd_integers = [n for i, n in enumerate(integers) if start_index <= i <= end_index and n % 2 != 0]
    return odd_integers