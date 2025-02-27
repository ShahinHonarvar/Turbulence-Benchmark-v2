def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(len(int_list)):
        if i >= 82 and i <= 86:
            if int_list[i] % 2 == 1:
                odd_ints.append(int_list[i])
    return odd_ints