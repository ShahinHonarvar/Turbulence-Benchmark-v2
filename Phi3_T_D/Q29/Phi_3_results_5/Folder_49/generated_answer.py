def gcf_two_nums(num_list):
    a = num_list[28]
    b = num_list[20]
    while b:
        a, b = (b, a % b)
    return a