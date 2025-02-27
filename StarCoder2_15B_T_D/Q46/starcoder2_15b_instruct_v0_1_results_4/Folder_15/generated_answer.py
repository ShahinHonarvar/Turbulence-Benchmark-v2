def gcf_three_nums(num_list):
    gcf = num_list[4]
    for i in num_list[0:4]:
        while i != 0:
            gcf, i = (i, gcf % i)
    for i in num_list[5:9]:
        while i != 0:
            gcf, i = (i, gcf % i)
    return gcf