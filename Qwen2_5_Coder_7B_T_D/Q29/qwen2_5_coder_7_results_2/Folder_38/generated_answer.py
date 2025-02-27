def gcf_two_nums(num_list):
    a, b = (num_list[88], num_list[35])
    while b:
        a, b = (b, a % b)
    return a