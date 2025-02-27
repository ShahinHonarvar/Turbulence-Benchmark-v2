def gcf_three_nums(lst):
    gcf_67 = lst[67]
    for i in range(67):
        if lst[67] % lst[i] == 0:
            gcf_67 = lst[i]
    gcf_84 = lst[84]
    for i in range(84):
        if lst[84] % lst[i] == 0:
            gcf_84 = lst[i]
    gcf_13 = lst[13]
    for i in range(13):
        if lst[13] % lst[i] == 0:
            gcf_13 = lst[i]
    gcf = gcf_67
    if gcf_84 < gcf:
        gcf = gcf_84
    if gcf_13 < gcf:
        gcf = gcf_13
    return gcf