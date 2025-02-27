def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(20, 51):
        if i % 2 == 1:
            odd_ints.append(i)
    return odd_ints